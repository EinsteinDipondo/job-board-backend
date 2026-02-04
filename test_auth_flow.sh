#!/bin/bash
echo "=== Complete Authentication Test ==="

# 1. Register a new user
echo -e "\n1. Registering new user..."
USERNAME="john_doe_$(date +%s)"
EMAIL="${USERNAME}@example.com"

REGISTER_RESPONSE=$(curl -s -X POST http://localhost:8000/api/auth/register/ \
  -H "Content-Type: application/json" \
  -d "{\"username\": \"$USERNAME\", \"email\": \"$EMAIL\", \"password\": \"password123\"}")

echo "Registration: $REGISTER_RESPONSE"

# 2. Login with the new user
echo -e "\n2. Logging in..."
LOGIN_RESPONSE=$(curl -s -X POST http://localhost:8000/api/auth/login/ \
  -H "Content-Type: application/json" \
  -c cookies.txt \
  -d "{\"username\": \"$USERNAME\", \"password\": \"password123\"}")

echo "Login: $LOGIN_RESPONSE"

# 3. Get current user info (with cookies)
echo -e "\n3. Getting current user info..."
ME_RESPONSE=$(curl -s http://localhost:8000/api/auth/me/ \
  -b cookies.txt)

echo "Current user: $ME_RESPONSE"

# 4. Create a job (authenticated)
echo -e "\n4. Creating a job (authenticated)..."
JOB_DATA='{
  "title": "Software Engineer Position",
  "description": "Looking for talented software engineers",
  "company_name": "Tech Innovations Inc",
  "location": "San Francisco, CA",
  "salary": "$120,000 - $150,000",
  "job_type": "Full-time",
  "category": 1
}'

CREATE_JOB_RESPONSE=$(curl -s -X POST http://localhost:8000/api/jobs/ \
  -H "Content-Type: application/json" \
  -b cookies.txt \
  -d "$JOB_DATA")

echo "Create job: $CREATE_JOB_RESPONSE"

# 5. Try to create job without authentication (should fail)
echo -e "\n5. Trying to create job without authentication (should fail)..."
UNAUTH_JOB_RESPONSE=$(curl -s -X POST http://localhost:8000/api/jobs/ \
  -H "Content-Type: application/json" \
  -d "$JOB_DATA")

echo "Unauthenticated create job: $UNAUTH_JOB_RESPONSE"

# 6. Logout
echo -e "\n6. Logging out..."
LOGOUT_RESPONSE=$(curl -s -X POST http://localhost:8000/api/auth/logout/ \
  -b cookies.txt)

echo "Logout: $LOGOUT_RESPONSE"

# 7. Clean up
rm -f cookies.txt

echo -e "\n✅ Authentication flow test complete!"
