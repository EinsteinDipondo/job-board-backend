from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
from .simple_auth import obtain_token, refresh_token
from .protected_api import protected_view, public_view

def home(request):
    return JsonResponse({
        'message': 'Job Board API',
        'status': 'running',
        'version': '1.0',
        'endpoints': {
            'home': '/',
            'admin': '/admin/',
            'public': '/api/public/',
            'protected': '/api/protected/ (Requires JWT)',
            'token_obtain': '/api/token/ (POST)',
            'token_refresh': '/api/token/refresh/ (POST)',
            'token_verify': '/api/token/verify/ (POST)',
        }
    })

urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    path('api/token/', obtain_token, name='token_obtain_pair'),
    path('api/token/refresh/', refresh_token, name='token_refresh'),
    path('api/protected/', protected_view, name='protected'),
    path('api/public/', public_view, name='public'),
]
