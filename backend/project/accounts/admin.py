from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import (UserCreationForm, UserChangeForm)
from accounts.models.user import User
from accounts.models.profiles.customer import customer_profile
from accounts.models.profiles.vendor import vendor_profile
from accounts.models.profiles.administrator import administrator_profile
from django.core.exceptions import ValidationError
from engine.engine import checkTestsForSlots

admin.site.site_header = 'Social Distancing Service - God Dashboard'

admin.site.register(customer_profile)


class vendorAdmin(admin.ModelAdmin):

    def save_related(self, request, form, formsets, change):
        super(vendorAdmin, self).save_related(request, form, formsets, change)
        # Check overlap here
        calendar = []

        for cal in form.instance.calendar.all():
            calendar.append(cal)

        resp = checkTestsForSlots(calendar)
        if resp == True:
            pass
        else:
            raise ValidationError("Error in slot")


admin.site.register(vendor_profile, vendorAdmin)
admin.site.register(administrator_profile)


class user_admin(UserAdmin):
    list_display = ('email', 'mode')
    list_filter = ('mode',)

    form = UserChangeForm
    add_form = UserCreationForm
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password',  'mode')}),
        ('Personal info', {'fields': ()}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'mode')}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(User, user_admin)
