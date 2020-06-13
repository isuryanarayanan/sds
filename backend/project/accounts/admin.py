from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import (UserCreationForm, UserChangeForm)
from accounts.models import User
from accounts.models import customer_profile, vendor_profile, administrator_profile

admin.site.site_header = 'Social Distancing Service - God Dashboard'

admin.site.register(customer_profile)
admin.site.register(vendor_profile)
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
