"""
Simple jobs API for frontend.
"""
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def jobs_list(request):
    """Return sample jobs data."""
    jobs = [
        {
            "id": 1,
            "title": "Senior React Developer",
            "company": "Tech Innovations Inc.",
            "location": "Remote",
            "salary": "$120,000 - $160,000",
            "type": "Full-time",
            "description": "Join our team to build cutting-edge web applications.",
            "posted": "2025-02-03",
            "requirements": ["5+ years React", "TypeScript", "REST APIs"]
        },
        {
            "id": 2,
            "title": "Python/Django Backend Engineer",
            "company": "Data Systems LLC",
            "location": "San Francisco, CA",
            "salary": "$130,000 - $170,000",
            "type": "Full-time",
            "description": "Build scalable backend systems for our platform.",
            "posted": "2025-02-04",
            "requirements": ["Python", "Django", "PostgreSQL", "AWS"]
        },
        {
            "id": 3,
            "title": "Full Stack Developer",
            "company": "Startup Ventures",
            "location": "New York, NY",
            "salary": "$100,000 - $140,000",
            "type": "Full-time",
            "description": "Work on both frontend and backend of our product.",
            "posted": "2025-02-05",
            "requirements": ["React", "Node.js", "MongoDB", "Docker"]
        },
        {
            "id": 4,
            "title": "DevOps Engineer",
            "company": "Cloud Solutions",
            "location": "Austin, TX",
            "salary": "$110,000 - $150,000",
            "type": "Full-time",
            "description": "Manage infrastructure and deployment pipelines.",
            "posted": "2025-02-06",
            "requirements": ["AWS", "Kubernetes", "Terraform", "CI/CD"]
        },
        {
            "id": 5,
            "title": "Frontend Developer",
            "company": "Digital Creations",
            "location": "Remote",
            "salary": "$90,000 - $130,000",
            "type": "Contract",
            "description": "Create beautiful user interfaces for web applications.",
            "posted": "2025-02-07",
            "requirements": ["JavaScript", "CSS", "UI/UX Design", "Responsive Design"]
        }
    ]
    return JsonResponse({"jobs": jobs, "count": len(jobs), "success": True})

@csrf_exempt
def job_detail(request, job_id):
    """Return details for a specific job."""
    # For now, just return a sample job
    job = {
        "id": job_id,
        "title": f"Job #{job_id} Details",
        "company": "Sample Company",
        "location": "Remote",
        "salary": "$100,000 - $150,000",
        "type": "Full-time",
        "description": "This is a detailed job description.",
        "posted": "2025-02-01",
        "requirements": ["Skill 1", "Skill 2", "Skill 3"],
        "responsibilities": ["Task 1", "Task 2", "Task 3"],
        "benefits": ["Health Insurance", "Remote Work", "Stock Options"]
    }
    return JsonResponse({"job": job, "success": True})
