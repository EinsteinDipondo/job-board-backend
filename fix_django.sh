#!/bin/bash
echo "=== Fixing Django Installation ==="

cd ~/desktop/job-board-backend

echo "1. Checking current setup..."
python --version 2>/dev/null || echo "Python not found"
which python

echo "2. Reactivating venv..."
deactivate 2>/dev/null || true
source venv/Scripts/activate 2>/dev/null || {
    echo "Ven activation failed. Recreating..."
    rm -rf venv
    "C:/Program Files/Python312/python.exe" -m venv venv
    source venv/Scripts/activate
}

echo "3. Installing Django..."
pip install django==5.0.2 --no-cache-dir

echo "4. Verifying..."
python -c "import django; print(f'✅ Django {django.__version__} installed')" 2>/dev/null || {
    echo "❌ Django not installed. Installing now..."
    pip install django==5.0.2 djangorestframework==3.14.0
}

echo "=== Done ==="
