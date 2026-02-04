from django.contrib import admin
from .models import JobCategory, Job

@admin.register(JobCategory)
class JobCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'company_name', 'location', 'category', 'posted_by', 'is_active', 'created_at')
    list_filter = ('is_active', 'category', 'created_at')
    search_fields = ('title', 'company_name', 'location', 'description')
    list_per_page = 20
    date_hierarchy = 'created_at'
    
    # Make the posted_by field read-only when editing
    readonly_fields = ('posted_by',)
    
    def save_model(self, request, obj, form, change):
        # Auto-set posted_by to current user if not set
        if not obj.posted_by_id:
            obj.posted_by = request.user
        super().save_model(request, obj, form, change)