from rest_framework import serializers
from .models import Job, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'description']
        read_only_fields = ['slug']

class JobSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), 
        source='category',
        write_only=True
    )
    posted_by = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = Job
        fields = [
            'id', 'title', 'description', 'company', 'location',
            'salary', 'job_type', 'category', 'category_id',
            'posted_by', 'is_active', 'created_at', 'updated_at'
        ]
        read_only_fields = ['posted_by', 'created_at', 'updated_at']
    
    def create(self, validated_data):
        validated_data['posted_by'] = self.context['request'].user
        return super().create(validated_data)

class JobFilterSerializer(serializers.Serializer):
    search = serializers.CharField(required=False)
    location = serializers.CharField(required=False)
    job_type = serializers.CharField(required=False)
    category = serializers.CharField(required=False)
    min_salary = serializers.DecimalField(required=False, max_digits=10, decimal_places=2)
    max_salary = serializers.DecimalField(required=False, max_digits=10, decimal_places=2)
