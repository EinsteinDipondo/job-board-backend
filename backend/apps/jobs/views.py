# backend/apps/jobs/views.py - REPLACE ENTIRE FILE WITH THIS
from rest_framework import viewsets, permissions, filters, status
from rest_framework.decorators import api_view, permission_classes, action
from rest_framework.response import Response
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Job, JobCategory, JobApplication
from .serializers import JobSerializer, JobCategorySerializer, JobApplicationSerializer, UserSerializer

# Existing authentication views (keep these)
@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def register_user(request):
    """Register a new user"""
    username = request.data.get('username')
    email = request.data.get('email')
    password = request.data.get('password')
    
    if not username or not email or not password:
        return Response(
            {'error': 'Username, email and password are required'},
            status=status.HTTP_400_BAD_REQUEST
        )
    
    if User.objects.filter(username=username).exists():
        return Response(
            {'error': 'Username already exists'},
            status=status.HTTP_400_BAD_REQUEST
        )
    
    if User.objects.filter(email=email).exists():
        return Response(
            {'error': 'Email already registered'},
            status=status.HTTP_400_BAD_REQUEST
        )
    
    user = User.objects.create_user(
        username=username,
        email=email,
        password=password
    )
    
    refresh = RefreshToken.for_user(user)
    
    return Response({
        'message': 'User created successfully',
        'user': {
            'id': user.id,
            'username': user.username,
            'email': user.email
        },
        'tokens': {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
    }, status=status.HTTP_201_CREATED)

@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def login_user(request):
    """Login user"""
    username = request.data.get('username')
    password = request.data.get('password')
    
    user = authenticate(username=username, password=password)
    
    if user is not None:
        login(request, user)
        refresh = RefreshToken.for_user(user)
        
        return Response({
            'message': 'Login successful',
            'user': {
                'id': user.id,
                'username': user.username,
                'email': user.email,
                'is_staff': user.is_staff
            },
            'tokens': {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }
        })
    else:
        return Response(
            {'error': 'Invalid credentials'},
            status=status.HTTP_401_UNAUTHORIZED
        )

@api_view(['POST'])
def logout_user(request):
    """Logout user"""
    logout(request)
    return Response({'message': 'Logout successful'})

@api_view(['GET'])
def current_user(request):
    """Get current user info"""
    if request.user.is_authenticated:
        return Response({
            'id': request.user.id,
            'username': request.user.username,
            'email': request.user.email,
            'is_staff': request.user.is_staff,
            'first_name': request.user.first_name,
            'last_name': request.user.last_name
        })
    else:
        return Response({'authenticated': False})

# Existing views (keep these)
class JobCategoryViewSet(viewsets.ModelViewSet):
    queryset = JobCategory.objects.all()
    serializer_class = JobCategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'description']

class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['category', 'location', 'job_type', 'is_active']
    search_fields = ['title', 'description', 'company_name', 'location']
    ordering_fields = ['created_at', 'title', 'salary']
    ordering = ['-created_at']
    
    def perform_create(self, serializer):
        serializer.save(posted_by=self.request.user)
    
    def get_queryset(self):
        # Filter by active jobs for non-staff users
        queryset = super().get_queryset()
        if not self.request.user.is_staff:
            queryset = queryset.filter(is_active=True)
        return queryset

# NEW VIEWS FOR JOB APPLICATIONS
class JobApplicationViewSet(viewsets.ModelViewSet):
    serializer_class = JobApplicationSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['job', 'status']
    
    def get_queryset(self):
        user = self.request.user
        queryset = JobApplication.objects.all()
        
        # Employers see applications for their jobs
        # Job seekers see their own applications
        if user.is_staff:
            return queryset
        elif Job.objects.filter(posted_by=user).exists():
            return queryset.filter(job__posted_by=user)
        else:
            return queryset.filter(applicant=user)
    
    def perform_create(self, serializer):
        serializer.save(applicant=self.request.user)

class MyApplicationsView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request):
        applications = JobApplication.objects.filter(applicant=request.user)
        serializer = JobApplicationSerializer(applications, many=True)
        return Response(serializer.data)