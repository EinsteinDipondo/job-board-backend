"""
Jobs API with CRUD operations and filtering.
"""
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json

# Sample jobs data - module-level variable
JOBS = [
    {
        "id": 1,
        "title": "Senior React Developer",
        "company": "Tech Innovations Inc.",
        "location": "San Francisco, CA",
        "salary": "$150,000 - $200,000",
        "type": "full_time",
        "category_id": 1,
        "description": "Lead frontend development with React and TypeScript.",
        "requirements": ["5+ years React", "TypeScript", "Redux"],
        "remote": True,
        "featured": True
    },
    {
        "id": 2,
        "title": "Backend Engineer",
        "company": "DataFlow Systems",
        "location": "Remote",
        "salary": "$130,000 - $180,000",
        "type": "full_time",
        "category_id": 1,
        "description": "Build scalable backend services with Django.",
        "requirements": ["Python", "Django", "PostgreSQL"],
        "remote": True,
        "featured": False
    }
]

@csrf_exempt
@require_http_methods(["GET", "POST"])
def jobs_list(request):
    """List all jobs or create a new job."""
    if request.method == 'GET':
        # Get filter parameters
        location = request.GET.get('location', '')
        job_type = request.GET.get('type', '')
        remote = request.GET.get('remote', '')
        search = request.GET.get('search', '')
        category = request.GET.get('category', '')
        
        filtered_jobs = JOBS
        
        # Apply filters
        if location:
            filtered_jobs = [j for j in filtered_jobs if location.lower() in j['location'].lower()]
        
        if job_type:
            filtered_jobs = [j for j in filtered_jobs if j['type'] == job_type]
        
        if remote.lower() == 'true':
            filtered_jobs = [j for j in filtered_jobs if j['remote']]
        
        if search:
            search = search.lower()
            filtered_jobs = [
                j for j in filtered_jobs 
                if search in j['title'].lower() 
                or search in j['description'].lower()
                or search in j['company'].lower()
            ]
        
        if category:
            filtered_jobs = [j for j in filtered_jobs if j['category_id'] == int(category)]
        
        return JsonResponse({
            "jobs": filtered_jobs,
            "count": len(filtered_jobs),
            "filters_applied": {
                "location": location,
                "type": job_type,
                "remote": remote,
                "search": search,
                "category": category
            }
        })
    
    elif request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            new_job = {
                "id": len(JOBS) + 1,
                "title": data.get('title', ''),
                "company": data.get('company', ''),
                "location": data.get('location', ''),
                "salary": data.get('salary', ''),
                "type": data.get('type', 'full_time'),
                "category_id": data.get('category_id', 1),
                "description": data.get('description', ''),
                "requirements": data.get('requirements', []),
                "remote": data.get('remote', False),
                "featured": data.get('featured', False)
            }
            JOBS.append(new_job)
            return JsonResponse(new_job, status=201)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

@csrf_exempt
@require_http_methods(["GET", "PUT", "DELETE"])
def job_detail(request, job_id):
    """Retrieve, update or delete a job."""
    job = next((j for j in JOBS if j['id'] == job_id), None)
    
    if not job:
        return JsonResponse({"error": "Job not found"}, status=404)
    
    if request.method == 'GET':
        return JsonResponse({"job": job})
    
    elif request.method == 'PUT':
        try:
            data = json.loads(request.body.decode('utf-8'))
            job.update({
                "title": data.get('title', job['title']),
                "company": data.get('company', job['company']),
                "location": data.get('location', job['location']),
                "salary": data.get('salary', job['salary']),
                "type": data.get('type', job['type']),
                "category_id": data.get('category_id', job['category_id']),
                "description": data.get('description', job['description']),
                "requirements": data.get('requirements', job['requirements']),
                "remote": data.get('remote', job['remote']),
                "featured": data.get('featured', job['featured'])
            })
            return JsonResponse({"job": job})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    
    elif request.method == 'DELETE':
        # Update the module-level variable
        JOBS[:] = [j for j in JOBS if j['id'] != job_id]
        return JsonResponse({"message": "Job deleted successfully"}, status=204)
