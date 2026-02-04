from django.contrib import admin
from .models import JobCategory, Job

@admin.register(JobCategory)
class JobCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    search_fields = ['name']

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ['title', 'company_name', 'location', 'job_type', 'is_active', 'created_at']
    list_filter = ['is_active', 'job_type', 'category', 'created_at']
    search_fields = ['title', 'company_name', 'location', 'description']
    list_editable = ['is_active']
