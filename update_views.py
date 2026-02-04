with open('backend/apps/jobs/views.py', 'r') as f:
    content = f.read()

# Update permission_classes for JobViewSet
new_content = content.replace(
    "permission_classes = [permissions.IsAuthenticatedOrReadOnly]",
    """permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    # Require authentication for write operations
    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [permissions.IsAuthenticated()]
        return super().get_permissions()"""
)

with open('backend/apps/jobs/views.py', 'w') as f:
    f.write(new_content)
print("✅ Updated JobViewSet permissions")
