#!/bin/bash
set -e

# Make migrations for made models
python manage.py makemigrations api

# Apply db migrations
echo "Apply database migrations"
python manage.py migrate

# Create super user
echo "Create database super user"
python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(username='admin').exists() or User.objects.create_superuser('admin', 'admin@gmail.com', 'pw')"

exec "$@"
