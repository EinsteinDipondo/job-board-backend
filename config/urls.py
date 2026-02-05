from django.contrib import admin
from django.urls import path
from django.http import JsonResponse
from .simple_auth import obtain_token
from .jobs_api import jobs_list, job_detail

def home(request):
    return JsonResponse({
        'message': 'Job Board API',
        'status': 'running',
        'version': '1.0',
        'frontend': 'https://heartfelt-frangollo-6c6478.netlify.app',
        'endpoints': {
            'home': '/',
            'admin': '/admin/',
            'token': '/api/token/ (POST)',
            'jobs_list': '/api/jobs/',
            'job_detail': '/api/jobs/<id>/',
        }
    })

urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    path('api/token/', obtain_token, name='token_obtain_pair'),
    path('api/jobs/', jobs_list, name='jobs_list'),
    path('api/jobs/<int:job_id>/', job_detail, name='job_detail'),
]
