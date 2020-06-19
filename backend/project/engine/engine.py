from django.core.exceptions import ValidationError


def check_overlap(self, fixed_start, fixed_end, new_start, new_end):
    print("the fuck")
    overlap = False
    if new_start == fixed_end or new_end == fixed_start:
        overlap = False
    elif (new_start >= fixed_start and new_start <= fixed_end) or (new_end >= fixed_start and new_end <= fixed_end):
        overlap = True
    elif new_start <= fixed_start and new_end >= fixed_end:
        overlap = True

    return overlap


def checkTestsForSlots(cal):
    elm = 0
    for i in range(0, len(cal)):

        if cal[i] != cal[elm]:
            if cal[i].end <= cal[i].start:
                raise ValidationError('Ending times must after starting times')

            if cal[elm].date == cal[i].date:
                if check_overlap(cal[i].start, cal[i].end, cal[elm].start, cal[elm].end):
                    raise ValidationError('There is an overlap with another event: ' + str(
                        cal[i].day) + ', ' + str(cal[i].start) + '-' + str(cal[i].end))

        elm = elm+1

    return True
