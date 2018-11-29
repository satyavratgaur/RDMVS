from django.contrib import admin

from login.models import UserCredentials
# Register your models here.

admin.site.register(UserCredentials)

class UsersAdmin(admin.ModelAdmin):
    pass
    #list_display = ('uname','psw')