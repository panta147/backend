from django.contrib import admin
from account.models import User, Otp
# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['uuid', 'email', 'first_name']


admin.site.register(Otp)
