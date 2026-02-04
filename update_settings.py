import re

with open('config/settings.py', 'r') as f:
    content = f.read()

# Add users app to INSTALLED_APPS if not already there
if "'backend.apps.users'" not in content:
    # Find INSTALLED_APPS and add users
    pattern = r"INSTALLED_APPS\s*=\s*\[(.*?)\]"
    match = re.search(pattern, content, re.DOTALL)
    
    if match:
        apps_section = match.group(1)
        # Add users before the closing bracket
        new_apps_section = apps_section.rstrip() + "\n    'backend.apps.users',\n"
        new_content = content[:match.start(1)] + new_apps_section + content[match.end(1):]
        
        # Also add AUTH_USER_MODEL
        if "AUTH_USER_MODEL" not in new_content:
            # Add after INSTALLED_APPS
            new_content = new_content.replace(
                "INSTALLED_APPS = [",
                "INSTALLED_APPS = [\n    'backend.apps.users',"
            )
            # Find a good place to add AUTH_USER_MODEL (after INSTALLED_APPS)
            inst_pos = new_content.find("INSTALLED_APPS = [")
            end_inst_pos = new_content.find("]", inst_pos)
            insert_pos = new_content.find("\n", end_inst_pos)
            new_content = new_content[:insert_pos] + "\n\nAUTH_USER_MODEL = 'users.User'\n" + new_content[insert_pos:]
        
        with open('config/settings.py', 'w') as f:
            f.write(new_content)
        print("✅ Added users app to settings.py")
    else:
        print("❌ Could not find INSTALLED_APPS")
else:
    print("✅ Users app already in INSTALLED_APPS")
