install environment first:
pip install django
pip install requests
pip install --upgrade google-api-python-client
after the environment set, plaese migrate the database:
python manage.py makemigrations tmdb
python manage.py migrate
after all set, you can started run it:
python manage.py runserver
