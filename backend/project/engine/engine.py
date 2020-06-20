from django.core.exceptions import ValidationError


def check_overlap(fixed_start, fixed_end, new_start, new_end):
    overlap = False
    if new_start == fixed_end or new_end == fixed_start:
        overlap = False
    elif (new_start >= fixed_start and new_start <= fixed_end) or (new_end >= fixed_start and new_end <= fixed_end):
        overlap = True
    elif new_start <= fixed_start and new_end >= fixed_end:
        overlap = True

    return overlap


def checkTestsForSlots(cal):
    res = True

    for xcal in cal:
        if xcal.end < xcal.start:
            res = False
        for ycal in cal:
            if xcal != ycal:
                if xcal.day == ycal.day:
                    if check_overlap(xcal.start, xcal.end, ycal.start, ycal.end):
                        res = False
    return res
