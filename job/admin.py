from django.contrib import admin

# Register your models here.
from . models import CompanyType,JobProvider,JobType

class CompanyTypeAdmin(admin.ModelAdmin):
    list_display=['uuid','name','created_at','updated_at']
admin.site.register(CompanyType,CompanyTypeAdmin)

class JobTypeAdmin(admin.ModelAdmin):
    list_display=['uuid','name','created_at','updated_at']

admin.site.register(JobType,JobTypeAdmin)



admin.site.register(JobProvider)



