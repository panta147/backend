from django.contrib import admin
from account.models import User
# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    # list_display = ["uuid", 'email', 'first_name','userType']
    # fieldsets = (
    #     ('General Info', {
    #         'fields': ('first_name','date', 'email','address','phone','userType','password')
    #     }),
    #     ('Permission', {
    #         'fields': ( 'is_staff', "is_active")
    #     }),
    # )
    list_display = ('email', 'first_name', 'address','phone','userType')
    list_filter = ('email', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password','first_name','date','address','phone','userType','companyName','companyType')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1' , 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)
