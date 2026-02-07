from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    USER_ROLES = [
        ('admin', 'Admin'),
        ('employer', 'Employer'),
        ('job_seeker', 'Job Seeker'),
    ]
    
    role = models.CharField(max_length=20, choices=USER_ROLES, default='job_seeker')
    phone = models.CharField(max_length=20, blank=True)
    company = models.CharField(max_length=200, blank=True)
    bio = models.TextField(blank=True)
    profile_picture = models.URLField(blank=True)
    
    class Meta:
        indexes = [
            models.Index(fields=['role']),
            models.Index(fields=['username']),
            models.Index(fields=['email']),
        ]
    
    def is_admin(self):
        return self.role == 'admin'
    
    def is_employer(self):
        return self.role == 'employer'
    
    def is_job_seeker(self):
        return self.role == 'job_seeker'
    
    def __str__(self):
        return f"{self.username} ({self.role})"
