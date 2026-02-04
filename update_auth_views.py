with open('backend/apps/jobs/views.py', 'r') as f:
    content = f.read()

# Replace the register_user view with CSRF exempt version
new_content = content.replace(
    """@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):""",
    """from django.views.decorators.csrf import csrf_exempt

@api_view(['POST'])
@permission_classes([AllowAny])
@csrf_exempt
def register_user(request):"""
)

# Replace the login_user view with CSRF exempt version
new_content = new_content.replace(
    """@api_view(['POST'])
@permission_classes([AllowAny])
def login_user(request):""",
    """@api_view(['POST'])
@permission_classes([AllowAny])
@csrf_exempt
def login_user(request):"""
)

# Replace the logout_user view with CSRF exempt version
new_content = new_content.replace(
    """@api_view(['POST'])
def logout_user(request):""",
    """@api_view(['POST'])
@csrf_exempt
def logout_user(request):"""
)

with open('backend/apps/jobs/views.py', 'w') as f:
    f.write(new_content)

print("✅ Updated authentication views with CSRF exempt")
