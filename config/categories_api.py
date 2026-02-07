"""
Categories API.
"""
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json

# Sample categories - define as a module-level variable
CATEGORIES = [
    {"id": 1, "name": "Software Development", "description": "Programming and engineering roles"},
    {"id": 2, "name": "Data Science", "description": "Data analysis and machine learning"},
    {"id": 3, "name": "DevOps", "description": "Infrastructure and operations"},
]

@csrf_exempt
@require_http_methods(["GET", "POST"])
def categories_list(request):
    if request.method == 'GET':
        return JsonResponse({"categories": CATEGORIES, "count": len(CATEGORIES)})
    
    elif request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            new_category = {
                "id": len(CATEGORIES) + 1,
                "name": data.get('name', ''),
                "description": data.get('description', '')
            }
            CATEGORIES.append(new_category)
            return JsonResponse(new_category, status=201)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

@csrf_exempt
@require_http_methods(["GET", "PUT", "DELETE"])
def category_detail(request, category_id):
    category = next((c for c in CATEGORIES if c['id'] == category_id), None)
    
    if not category:
        return JsonResponse({"error": "Category not found"}, status=404)
    
    if request.method == 'GET':
        return JsonResponse({"category": category})
    
    elif request.method == 'PUT':
        try:
            data = json.loads(request.body.decode('utf-8'))
            category.update({
                "name": data.get('name', category['name']),
                "description": data.get('description', category['description'])
            })
            return JsonResponse({"category": category})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    
    elif request.method == 'DELETE':
        # Use the module-level variable
        CATEGORIES[:] = [c for c in CATEGORIES if c['id'] != category_id]
        return JsonResponse({"message": "Category deleted successfully"}, status=204)
