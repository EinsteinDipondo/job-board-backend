"""
Simple URL patterns for jobs app - avoids import-time issues.
"""
from django.urls import path

# Don't import anything from rest_framework here
# We'll define patterns in a function

def get_job_urlpatterns():
    """Get URL patterns - called when Django is ready."""
    from rest_framework.routers import DefaultRouter
    from .views import (
        JobViewSet, JobCategoryViewSet, JobApplicationViewSet,
        register_user, login_user, logout_user, current_user,
        MyApplicationsView
    )
    
    router = DefaultRouter()
    router.register(r'jobs', JobViewSet, basename='job')
    router.register(r'categories', JobCategoryViewSet, basename='jobcategory')
    router.register(r'applications', JobApplicationViewSet, basename='jobapplication')
    
    from django.urls import include
    return [
        path('', include(router.urls)),
        path('auth/register/', register_user, name='register'),
        path('auth/login/', login_user, name='login'),
        path('auth/logout/', logout_user, name='logout'),
        path('auth/me/', current_user, name='current_user'),
        path('my-applications/', MyApplicationsView.as_view(), name='my_applications'),
    ]

# This is what Django will import
urlpatterns = get_job_urlpatterns()
