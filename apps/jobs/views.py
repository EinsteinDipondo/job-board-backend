from rest_framework import viewsets, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q
from .models import Job, Category
from .serializers import JobSerializer, CategorySerializer, JobFilterSerializer
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]
    lookup_field = 'slug'

class JobViewSet(viewsets.ModelViewSet):
    serializer_class = JobSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['job_type', 'category', 'location']
    search_fields = ['title', 'description', 'company']
    ordering_fields = ['salary', 'created_at', 'title']
    ordering = ['-created_at']
    
    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [permissions.IsAuthenticated(), IsOwnerOrReadOnly()]
        return [permissions.AllowAny()]
    
    def get_queryset(self):
        queryset = Job.objects.filter(is_active=True)
        
        # Advanced filtering
        filter_serializer = JobFilterSerializer(data=self.request.query_params)
        if filter_serializer.is_valid():
            data = filter_serializer.validated_data
            
            if data.get('search'):
                queryset = queryset.filter(
                    Q(title__icontains=data['search']) |
                    Q(description__icontains=data['search']) |
                    Q(company__icontains=data['search'])
                )
            
            if data.get('location'):
                queryset = queryset.filter(location__icontains=data['location'])
            
            if data.get('job_type'):
                queryset = queryset.filter(job_type=data['job_type'])
            
            if data.get('category'):
                queryset = queryset.filter(category__slug=data['category'])
            
            if data.get('min_salary'):
                queryset = queryset.filter(salary__gte=data['min_salary'])
            
            if data.get('max_salary'):
                queryset = queryset.filter(salary__lte=data['max_salary'])
        
        return queryset.select_related('category', 'posted_by')
