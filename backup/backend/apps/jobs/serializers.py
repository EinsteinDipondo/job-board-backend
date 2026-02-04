from rest_framework import serializers
from .models import Job, JobCategory

class JobCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = JobCategory
        fields = ['id', 'name']

class JobSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)
    posted_by_name = serializers.CharField(source='posted_by.username', read_only=True)
    
    class Meta:
        model = Job
        fields = [
            'id', 'title', 'description', 'company_name', 
            'location', 'salary', 'category', 'category_name',
            'posted_by', 'posted_by_name', 'is_active', 'created_at'
        ]
        read_only_fields = ['posted_by', 'created_at']