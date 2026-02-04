# backend/apps/jobs/urls.py - REPLACE ENTIRE FILE WITH THIS
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    JobViewSet, JobCategoryViewSet, JobApplicationViewSet,  # ADD JobApplicationViewSet
    register_user, login_user, logout_user, current_user,
    MyApplicationsView  # ADD MyApplicationsView
)

router = DefaultRouter()
router.register(r'jobs', JobViewSet, basename='job')
router.register(r'categories', JobCategoryViewSet, basename='jobcategory')
router.register(r'applications', JobApplicationViewSet, basename='jobapplication')  # NEW

urlpatterns = [
    path('', include(router.urls)),
    path('auth/register/', register_user, name='register'),
    path('auth/login/', login_user, name='login'),
    path('auth/logout/', logout_user, name='logout'),
    path('auth/me/', current_user, name='current_user'),
    path('my-applications/', MyApplicationsView.as_view(), name='my_applications'),  # NEW
]