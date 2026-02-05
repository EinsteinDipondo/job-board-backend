
@csrf_exempt
def refresh_token(request):
    """
    Refresh JWT token endpoint.
    """
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            refresh_token_str = data.get('refresh', '')
            
            if not refresh_token_str:
                return JsonResponse({'error': 'Refresh token required'}, status=400)
            
            refresh = RefreshToken(refresh_token_str)
            
            # Verify the refresh token is valid
            try:
                refresh.verify()
            except Exception as e:
                return JsonResponse({'error': 'Invalid refresh token'}, status=401)
            
            # Generate new access token
            new_access = refresh.access_token
            
            return JsonResponse({
                'access': str(new_access),
            })
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'error': 'Method not allowed'}, status=405)

@csrf_exempt
def verify_token(request):
    """
    Verify JWT token endpoint.
    """
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            token = data.get('token', '')
            
            if not token:
                return JsonResponse({'error': 'Token required'}, status=400)
            
            # Try to decode and verify
            try:
                from rest_framework_simplejwt.tokens import AccessToken
                validated_token = AccessToken(token)
                validated_token.verify()
                return JsonResponse({'message': 'Token is valid'})
            except Exception as e:
                return JsonResponse({'error': 'Token is invalid'}, status=401)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'error': 'Method not allowed'}, status=405)
