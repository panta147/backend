from django.contrib import admin

# Register your models here.
from . models import CompanyType
class CompanyTypeAdmin(admin.ModelAdmin):
    list_display=['uuid','name','created_at','updated_at']
admin.site.register(CompanyType,CompanyTypeAdmin)