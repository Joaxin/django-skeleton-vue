django-skeleton-vue

## Features

- Django restframwork
- admin simpleui
- taggit
- debug_toolbar
- Vue CLI3 & Vue.js integration
- vue-resource, element-ui

## Setup

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

## Vue

Node.js from http://nodejs.cn/download/

```
node -v
	v12.10.0
npm install npm -g
npm -v
	6.11.3
```

```
# Not needed here
# vue-cli ==> @vue/cli
# ✘ npm install -g vue-cli
# ✘ vue-init webpack vuefront
```

```
npm install -g @vue/cli
vue -V
	3.11.0

## Will  Use https://registry.npm.taobao.org for faster installation in China
vue create vuefront 

# Vue CLI v3.11.0
# ? Check the features needed for your project: Babel, Router, Vuex, CSS Pre-processors, # Linter
# ? Use history mode for router? (Requires proper server setup for index fallback in # production) No
# ? Pick a CSS pre-processor (PostCSS, Autoprefixer and CSS Modules are supported by # default): Sass/SCSS(with dart-sass)
# ? Pick a linter / formatter config: Prettier
# ? Pick additional lint features: Lint on save
# ? Where do you prefer placing config for Babel, PostCSS, ESLint, etc.? In dedicated # config files
# ? Save this as a preset for future projects? Yes
```

```
cd vuefront
# install dependencies
npm install
npm install  vue-resource
npm install element-ui
```

Project setup
```
npm install
```

Compiles and hot-reloads for development
```
npm run serve
```

Compiles and minifies for production
```
npm run build
```
Run your tests
```
npm run test
```

Lints and fixes files
```
npm run lint
```

Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/)



## REFERENCES

- .browserslistrc ==> https://github.com/browserslist/browserslist#custom-usage-data

https://cli.vuejs.org/config/#typescript

