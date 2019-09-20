# django-skeleton-vue
a vue.js template for django

setup a `virtualenv` if needed

```
mkdir env
virtualenv dj
source dj/bin/activate
cd yourproject
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
```

Create a superuser:

```
python manage.py createsuperuser
username:demo
passwordLdemodemo
```

Run:

```
python manage.py runserver
```

Load the site at [http://127.0.0.1:8000](http://127.0.0.1:8000/).


pip install psycopg2
