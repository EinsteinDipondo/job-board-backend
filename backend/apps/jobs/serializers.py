# backend/apps/jobs/serializers.py - REPLACE ENTIRE FILE WITH THIS
from rest_framework import serializers
from .models import Job, JobCategory, JobApplication
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'is_staff']
        read_only_fields = ['id', 'is_staff']

class JobCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = JobCategory
        fields = ['id', 'name', 'description']
        read_only_fields = ['id']

class JobSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)
    posted_by = UserSerializer(read_only=True)
    
    class Meta:
        model = Job
        fields = [
            'id', 'title', 'description', 'company_name', 'location',
            'salary', 'job_type', 'category', 'category_name',
            'posted_by', 'is_active', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'posted_by', 'created_at', 'updated_at']

class JobApplicationSerializer(serializers.ModelSerializer):  # NEW SERIALIZER
    job_title = serializers.CharField(source='job.title', read_only=True)
    applicant_name = serializers.CharField(source='applicant.username', read_only=True)
    resume_url = serializers.SerializerMethodField()
    
    class Meta:
        model = JobApplication
        fields = [
            'id', 'job', 'job_title', 'applicant', 'applicant_name',
            'cover_letter', 'resume', 'resume_url', 'status', 
            'applied_at', 'notes'
        ]
        read_only_fields = ['applicant', 'applied_at']
    
    def get_resume_url(self, obj):
        if obj.resume:
            return obj.resume.url
        return None
    
    def validate(self, data):
        # Check if user already applied
        user = self.context['request'].user
        job = data.get('job') or self.instance.job if self.instance else None
        
        if job and JobApplication.objects.filter(job=job, applicant=user).exists():
            raise serializers.ValidationError("You have already applied for this job")
        
        return data