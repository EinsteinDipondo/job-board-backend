import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.db import connection

# Create tables manually if needed
with connection.cursor() as cursor:
    try:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS auth_user (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                password VARCHAR(128) NOT NULL,
                last_login DATETIME NULL,
                is_superuser BOOLEAN NOT NULL,
                username VARCHAR(150) NOT NULL UNIQUE,
                first_name VARCHAR(150) NOT NULL,
                last_name VARCHAR(150) NOT NULL,
                email VARCHAR(254) NOT NULL,
                is_staff BOOLEAN NOT NULL,
                is_active BOOLEAN NOT NULL,
                date_joined DATETIME NOT NULL
            )
        """)
        print("✅ Created auth_user table")
    except Exception as e:
        print(f"Note: {e}")

print("✅ Database setup complete")
