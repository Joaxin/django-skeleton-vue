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

### Vue



```
npm install -g vue-cli
vue-init webpack vuefront
cd vuefront
# install dependencies
npm install
npm install --save vuex

npm install  vue-resource
npm install element-ui
```

```
# serve with hot reload at localhost:8080
npm run dev

# build for production with minification
npm run build

# build for production and view the bundle analyzer report
npm run build --report

# run unit tests
npm run unit

# run e2e tests
npm run e2e

# run all tests
npm test
```

