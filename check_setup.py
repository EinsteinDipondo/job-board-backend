import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.db import connection

print("=== Checking Database Setup ===")

# Check if tables exist
with connection.cursor() as cursor:
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name LIKE 'jobs_%';")
    tables = cursor.fetchall()
    
    print(f"Found {len(tables)} jobs tables:")
    for table in tables:
        print(f"  - {table[0]}")

# Check if jobs app is in INSTALLED_APPS
from django.conf import settings
if 'backend.apps.jobs' in settings.INSTALLED_APPS:
    print("✅ Jobs app is in INSTALLED_APPS")
else:
    print("❌ Jobs app NOT in INSTALLED_APPS")
    print(f"Current apps: {settings.INSTALLED_APPS}")

# Try to import jobs models
try:
    from backend.apps.jobs.models import Job, JobCategory
    print("✅ Jobs models imported successfully")
except Exception as e:
    print(f"❌ Error importing jobs models: {e}")
