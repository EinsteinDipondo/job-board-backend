#!/bin/bash
echo "=== Creating Job Categories ==="

# Get a fresh JWT token
TOKEN_RESPONSE=$(curl -s -X POST http://localhost:8000/api/token/ \
  -H "Content-Type: application/json" \
  -d '{"username": "testuser", "password": "testpass123"}')

ACCESS_TOKEN=$(echo "$TOKEN_RESPONSE" | python -c "
import json, sys
try:
    data = json.load(sys.stdin)
    print(data['access'])
except:
    print('')
")

echo "Using token: ${ACCESS_TOKEN:0:30}..."

# Categories to create
categories=(
    '{"name": "Software Development", "description": "Programming and software engineering roles"}'
    '{"name": "Marketing", "description": "Marketing and advertising positions"}'
    '{"name": "Design", "description": "UI/UX and graphic design roles"}'
    '{"name": "Sales", "description": "Sales and business development"}'
    '{"name": "Finance", "description": "Finance and accounting positions"}'
    '{"name": "Healthcare", "description": "Medical and healthcare roles"}'
    '{"name": "Education", "description": "Teaching and educational positions"}'
)

for category in "${categories[@]}"; do
    echo "Creating category: $category"
    curl -s -X POST http://localhost:8000/api/categories/ \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer $ACCESS_TOKEN" \
      -d "$category"
    echo ""
done

echo -e "\n✅ Categories created!"
echo "Now you can create jobs with category IDs 1-7"
