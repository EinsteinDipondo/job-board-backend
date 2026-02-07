from django.db import models
from django.contrib.auth import get_user_model
from apps.jobs.models import Job

User = get_user_model()

APPLICATION_STATUS = [
    ('pending', 'Pending'),
    ('reviewed', 'Reviewed'),
    ('shortlisted', 'Shortlisted'),
    ('rejected', 'Rejected'),
    ('accepted', 'Accepted'),
]

class Application(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='applications')
    applicant = models.ForeignKey(User, on_delete=models.CASCADE, related_name='applications')
    cover_letter = models.TextField()
    resume_url = models.URLField(blank=True)
    status = models.CharField(max_length=20, choices=APPLICATION_STATUS, default='pending')
    applied_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-applied_at']
        unique_together = ['job', 'applicant']
        indexes = [
            models.Index(fields=['status']),
            models.Index(fields=['applied_at']),
            models.Index(fields=['job', 'applicant']),
        ]
    
    def __str__(self):
        return f"{self.applicant.username} applied for {self.job.title}"
