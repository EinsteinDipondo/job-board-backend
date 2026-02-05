from django.contrib import admin
from django.urls import path
from django.http import JsonResponse
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
import json

def home(request):
    return JsonResponse({
        'message': 'Job Board API',
        'status': 'running',
        'version': '1.0'
    })

@csrf_exempt
def obtain_token(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            username = data.get('username')
            password = data.get('password')
            
            user = authenticate(username=username, password=password)
            if user:
                refresh = RefreshToken.for_user(user)
                return JsonResponse({
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                })
            else:
                return JsonResponse({'error': 'Invalid credentials'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'error': 'Method not allowed'}, status=405)

urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    path('api/token/', obtain_token),
    path('api/token/refresh/', lambda r: JsonResponse({'error': 'Not implemented'}, status=501)),
]
from django.http import JsonResponse
import json
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def register_user(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            username = data.get('username')
            password = data.get('password')
            email = data.get('email', '')
            
            if User.objects.filter(username=username).exists():
                return JsonResponse({'error': 'Username exists'}, status=400)
            
            user = User.objects.create_user(username, email, password)
            return JsonResponse({'message': 'User created', 'username': username})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'error': 'Method not allowed'}, status=405)
