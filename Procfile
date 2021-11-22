release: python manage.py makemigrations
release: python manage.py migrate
web: gunicorn Webbooks.wsgi --log-file -
