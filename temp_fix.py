# Add this near the top of settings.py, after other imports
try:
    import dj_database_url
    HAS_DJ_DATABASE_URL = True
except ImportError:
    HAS_DJ_DATABASE_URL = False
    print("Note: dj-database-url not installed, using SQLite fallback")
