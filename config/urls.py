from django.contrib import admin
from django.urls import path
from django.http import JsonResponse
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

def home(request):
    return JsonResponse({
        'message': 'Job Board API',
        'status': 'running',
        'version': '1.0',
        'endpoints': {
            'admin': '/admin/',
            'token': '/api/token/',
            'token_refresh': '/api/token/refresh/',
        }
    })

urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
