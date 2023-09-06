# Install dependencies
pip install --upgrade pip
pip install -r deps.txt


# static files
python manage.py collectstatic --no-input
# Run migrations
python manage.py migrate