import requests
import json

BASE_URL = "http://localhost:8000/api"

def test_auth():
    print("=== Testing Authentication ===")
    
    # Test 1: Get CSRF token
    print("\n1. Getting CSRF token...")
    response = requests.get(f"{BASE_URL}/auth/me/")
    print(f"Current user: {response.json()}")
    
    # Test 2: Register new user
    print("\n2. Registering new user...")
    user_data = {
        'username': 'testuser',
        'email': 'test@example.com',
        'password': 'testpass123'
    }
    
    response = requests.post(f"{BASE_URL}/auth/register/", json=user_data)
    print(f"Register response: {response.status_code}")
    if response.status_code == 201:
        print(f"User created: {response.json()}")
    else:
        print(f"Error: {response.json()}")
    
    # Test 3: Login
    print("\n3. Logging in...")
    login_data = {
        'username': 'testuser',
        'password': 'testpass123'
    }
    
    # Create a session to maintain cookies
    session = requests.Session()
    response = session.post(f"{BASE_URL}/auth/login/", json=login_data)
    print(f"Login response: {response.status_code}")
    if response.status_code == 200:
        print(f"Login successful: {response.json()}")
    else:
        print(f"Error: {response.json()}")
    
    # Test 4: Get current user after login
    print("\n4. Getting current user after login...")
    response = session.get(f"{BASE_URL}/auth/me/")
    print(f"Current user: {response.json()}")
    
    # Test 5: Create a job (authenticated)
    print("\n5. Creating a job (authenticated)...")
    job_data = {
        'title': 'Test Developer Position',
        'description': 'Test job description',
        'company_name': 'Test Company',
        'location': 'Remote',
        'salary': '$80,000',
        'job_type': 'Full-time',
        'category': 1  # Assuming category 1 exists
    }
    
    response = session.post(f"{BASE_URL}/jobs/", json=job_data)
    print(f"Create job response: {response.status_code}")
    if response.status_code == 201:
        print(f"Job created: {response.json()}")
    else:
        print(f"Error: {response.json()}")
    
    # Test 6: Logout
    print("\n6. Logging out...")
    response = session.post(f"{BASE_URL}/auth/logout/")
    print(f"Logout response: {response.status_code}")
    print(f"Message: {response.json()}")

if __name__ == "__main__":
    test_auth()
