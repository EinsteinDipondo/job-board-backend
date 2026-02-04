import re

with open('config/settings.py', 'r') as f:
    content = f.read()

# Find INSTALLED_APPS section
pattern = r'INSTALLED_APPS\s*=\s*\[(.*?)\]'
match = re.search(pattern, content, re.DOTALL)

if match:
    apps_section = match.group(1)
    
    # Split by lines and clean up
    lines = [line.strip() for line in apps_section.split('\n')]
    
    # Remove duplicates and keep only backend.apps.users
    unique_apps = []
    has_users = False
    has_backend_users = False
    
    for line in lines:
        if line and not line.startswith('#'):
            if "'users'" in line and not "'backend.apps.users'" in line:
                # Skip plain 'users'
                print(f"Removing duplicate: {line}")
                continue
            elif "'backend.apps.users'" in line:
                if not has_backend_users:
                    unique_apps.append(line)
                    has_backend_users = True
                else:
                    print(f"Removing duplicate backend.apps.users: {line}")
            else:
                unique_apps.append(line)
    
    # Rebuild the list
    new_apps_section = "    " + ",\n    ".join(unique_apps) + ","
    
    # Replace in content
    new_content = content[:match.start(1)] + "\n" + new_apps_section + "\n" + content[match.end(1):]
    
    with open('config/settings.py', 'w') as f:
        f.write(new_content)
    
    print("✅ Fixed duplicate users app")
    print("Current apps:", unique_apps)
else:
    print("❌ Could not find INSTALLED_APPS")
