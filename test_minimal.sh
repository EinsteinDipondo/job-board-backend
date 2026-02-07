#!/bin/bash

BASE_URL="https://job-board-backend-z5ul.onrender.com"
echo "Testing minimal deployment..."
echo "============================="

echo "1. Waiting 60 seconds for deployment..."
sleep 60

echo "2. Testing homepage:"
for i in {1..10}; do
    response=$(curl -s -o /dev/null -w "%{http_code}" "$BASE_URL" || echo "curl_failed")
    if [ "$response" = "200" ]; then
        echo "✅ Homepage is up (HTTP 200)"
        curl -s "$BASE_URL" | head -c 200
        echo ""
        break
    elif [ "$response" = "500" ]; then
        echo "❌ Still getting 500 error"
    else
        echo "⚠️  Got HTTP $response, waiting..."
    fi
    sleep 10
done

echo ""
echo "3. Testing token endpoint:"
curl -s "$BASE_URL/api/token/"
echo ""

echo "4. Testing token POST (minimal):"
curl -X POST "$BASE_URL/api/token/" \
  -H "Content-Type: application/json" \
  -d '{"test": "data"}' \
  -w "\nHTTP Status: %{http_code}\n"
