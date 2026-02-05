"""
Protected API endpoint for testing.
"""
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import InvalidToken, AuthenticationFailed
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
import json

@csrf_exempt
def protected_view(request):
    """
    Simple protected endpoint that requires JWT authentication.
    """
    # Try to authenticate
    jwt_auth = JWTAuthentication()
    try:
        validated_token = jwt_auth.get_validated_token(request)
        user = jwt_auth.get_user(validated_token)
        
        if user:
            return JsonResponse({
                'message': 'Access granted',
                'user': {
                    'id': user.id,
                    'username': user.username,
                    'email': user.email if hasattr(user, 'email') else None,
                },
                'protected_data': 'This is sensitive data only visible to authenticated users.',
            })
        else:
            return JsonResponse({'error': 'Invalid user'}, status=401)
    except (InvalidToken, AuthenticationFailed) as e:
        return JsonResponse({'error': 'Invalid or expired token'}, status=401)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)

@csrf_exempt
def public_view(request):
    """
    Public endpoint that doesn't require authentication.
    """
    return JsonResponse({
        'message': 'Public endpoint',
        'data': 'Anyone can access this.',
    })
