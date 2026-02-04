#!/bin/bash
echo "=== Testing with Valid Token ==="

# Use your actual token
ACCESS_TOKEN="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzcwMzA1MzE2LCJpYXQiOjE3NzAyMTg5MTYsImp0aSI6ImEyODNiZmFjZWJlMzRjNTI5M2U2MTZmOTQyOWM3YjAzIiwidXNlcl9pZCI6IjIifQ.0UGTNMIZtD_IPoqkHNmvT5w2NrAy5lAQeqBLvlkbnYQ"

echo "Using token: ${ACCESS_TOKEN:0:50}..."

# 1. Test token validity
echo -e "\n1. Testing token validity..."
curl -s -H "Authorization: Bearer $ACCESS_TOKEN" \
  http://localhost:8000/api/auth/me/ | python -m json.tool

# 2. Get first job ID
echo -e "\n2. Getting first job ID..."
JOB_RESPONSE=$(curl -s http://localhost:8000/api/jobs/)

JOB_ID=$(echo "$JOB_RESPONSE" | python -c "
import json, sys
try:
    data = json.load(sys.stdin)
    if isinstance(data, list):
        if len(data) > 0:
            print(data[0]['id'])
        else:
            print('1')
    elif isinstance(data, dict) and 'results' in data:
        if len(data['results']) > 0:
            print(data['results'][0]['id'])
        else:
            print('1')
    else:
        print('1')
except Exception as e:
    print('1')
")

echo "Found job ID: $JOB_ID"

# 3. Create application
echo -e "\n3. Creating job application..."
APPLICATION_DATA='{
    "job": '$JOB_ID',
    "cover_letter": "Dear Hiring Manager,\n\nI am writing to express my interest in the position. I have extensive experience and am confident I can contribute to your team.\n\nBest regards,\nTest Applicant",
    "status": "pending"
}'

APPLICATION_RESPONSE=$(curl -s -X POST http://localhost:8000/api/applications/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $ACCESS_TOKEN" \
  -d "$APPLICATION_DATA")

echo "Application response:"
echo "$APPLICATION_RESPONSE" | python -m json.tool 2>/dev/null || echo "$APPLICATION_RESPONSE"

# 4. Get my applications
echo -e "\n4. Getting my applications..."
MY_APPS=$(curl -s -H "Authorization: Bearer $ACCESS_TOKEN" \
  http://localhost:8000/api/my-applications/)

echo "My applications:"
echo "$MY_APPS" | python -m json.tool 2>/dev/null || echo "$MY_APPS"

# 5. Try to get ALL applications (for employer/admin)
echo -e "\n5. Getting all applications (if employer)..."
ALL_APPS=$(curl -s -H "Authorization: Bearer $ACCESS_TOKEN" \
  http://localhost:8000/api/applications/)

echo "All applications:"
echo "$ALL_APPS" | python -c "
import json, sys
try:
    data = json.load(sys.stdin)
    if isinstance(data, list):
        print(f'Found {len(data)} applications')
        for app in data[:3]:  # Show first 3
            print(f'  - {app.get(\"id\")}: {app.get(\"job_title\")} ({app.get(\"status\")})')
    elif isinstance(data, dict) and 'results' in data:
        print(f'Found {len(data[\"results\"])} applications')
        for app in data['results'][:3]:
            print(f'  - {app.get(\"id\")}: {app.get(\"job_title\")} ({app.get(\"status\")})')
    else:
        print('No applications found or unauthorized')
except:
    print('Could not parse response')
"

echo -e "\n✅ Test Complete!"
