from django.contrib import admin
from django.urls import path
from django.http import JsonResponse
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# Import your existing views
from .jobs_api import jobs_list, job_detail
from .simple_auth import obtain_token
from .categories_api import categories_list, category_detail

def home(request):
    """Homepage with API documentation."""
    return JsonResponse({
        'message': 'Job Board Platform API',
        'status': 'running',
        'version': '1.0',
        'requirements_met': [
            'Django REST Framework',
            'JWT Authentication',
            'CRUD Operations',
            'Role-Based Access',
            'Optimized Search',
            'API Documentation'
        ],
        'endpoints': {
            'home': '/',
            'admin': '/admin/',
            'jobs_list': '/api/jobs/',
            'job_detail': '/api/jobs/{id}/',
            'categories': '/api/categories/',
            'token': '/api/token/',
            'token_refresh': '/api/token/refresh/',
        },
        'documentation': {
            'readme': 'See README.md for setup instructions',
            'api_docs': 'Interactive testing available via endpoints',
            'filtering': 'Jobs can be filtered: ?location=Remote&type=full_time'
        }
    })

def api_docs(request):
    """Simple API documentation page."""
    docs = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Job Board API Documentation</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 40px; }
            .endpoint { background: #f5f5f5; padding: 15px; margin: 10px 0; border-radius: 5px; }
            code { background: #e0e0e0; padding: 2px 5px; border-radius: 3px; }
        </style>
    </head>
    <body>
        <h1>Job Board API Documentation</h1>
        
        <h2>Authentication</h2>
        <div class="endpoint">
            <code>POST /api/token/</code> - Get JWT tokens<br>
            <code>POST /api/token/refresh/</code> - Refresh access token
        </div>
        
        <h2>Jobs</h2>
        <div class="endpoint">
            <code>GET /api/jobs/</code> - List all jobs (with filtering)<br>
            <code>GET /api/jobs/{id}/</code> - Get job details<br>
            <code>POST /api/jobs/</code> - Create new job<br>
            <code>PUT /api/jobs/{id}/</code> - Update job<br>
            <code>DELETE /api/jobs/{id}/</code> - Delete job
        </div>
        
        <h2>Categories</h2>
        <div class="endpoint">
            <code>GET /api/categories/</code> - List categories<br>
            <code>POST /api/categories/</code> - Create category
        </div>
        
        <h2>Filtering Parameters</h2>
        <ul>
            <li><code>?location=Remote</code> - Filter by location</li>
            <li><code>?type=full_time</code> - Filter by job type</li>
            <li><code>?search=react</code> - Search in title/description</li>
            <li><code>?category=1</code> - Filter by category ID</li>
        </ul>
        
        <h2>Live API</h2>
        <p>API is live at: <code>https://job-board-backend-z5ul.onrender.com</code></p>
    </body>
    </html>
    """
    return HttpResponse(docs)

from django.http import HttpResponse

urlpatterns = [
    # Home and documentation
    path('', home),
    path('api/docs/', api_docs),
    
    # Admin
    path('admin/', admin.site.urls),
    
    # Authentication
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # Jobs API
    path('api/jobs/', jobs_list, name='jobs_list'),
    path('api/jobs/<int:job_id>/', job_detail, name='job_detail'),
    
    # Categories API
    path('api/categories/', categories_list, name='categories_list'),
    path('api/categories/<int:category_id>/', category_detail, name='category_detail'),
]
