"""
Simple JWT token endpoint - minimal error handling.
"""
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def obtain_token(request):
    """
    Return a simple response to confirm the endpoint exists.
    We'll add full JWT logic after we confirm it works.
    """
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            return JsonResponse({
                'message': 'Token endpoint is working',
                'received_data': data,
                'next_step': 'Full JWT implementation pending'
            })
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        # Return method info for GET requests
        return JsonResponse({
            'message': 'Token endpoint',
            'method': 'POST only',
            'required_fields': ['username', 'password']
        }, status=405)
