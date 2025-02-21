web: gunicorn djangobasico.wsgi:application --workers=1 --threads=2 --timeout 120 --log-level=debug

release: python manage.py collectstatic --noinput