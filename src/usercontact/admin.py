from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from usercontact.models import UserProfile
from django.contrib import admin

class UserProfileInline(admin.StackedInline):
    model = UserProfile
    fieldsets = [
        (None, {'fields':['contact_pref', 'phone_number', 'phone_provider', 'gen_sms_field']})
    ]
    readonly_fields=['gen_sms_field']

class UserProfileAdmin(UserAdmin):
    list_display = ('username','email','last_name', 'first_name', 'date_joined', 'id')
    inlines = [UserProfileInline]

admin.site.unregister(User)
admin.site.register(User, UserProfileAdmin)