from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
import json

@csrf_exempt
def register_user(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            username = data.get('username', '')
            password = data.get('password', '')
            email = data.get('email', '')
            
            # Create user
            user = User.objects.create_user(username, email, password)
            user.save()
            
            return JsonResponse({
                'message': 'User created successfully',
                'username': username
            })
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'error': 'Method not allowed'}, status=405)
