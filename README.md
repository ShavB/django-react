# main
### Reference
https://pypi.org/x

# Django React


# 1. Python virtial environment
python3 -m venv env
source env/bin/activate

# install Django
pip3 install django
pip3 install django-cors-headers
pip install djangorestframework

# start project
django-admin startproject backend
cd backend
python3 manage.py startapp api

#Get started with react
#### will be using vite for react
    npm create vite@latest
    cd 'name of the app'
    npm i or npm start

# bootup the server
    cd backend
    python3 manage.py runserver
# bootup client
    cd ..
    cd frontend
    npm run dev

# enable cors
If following the below project structure.

# folder/project structure
    In the project structure
    ├── backend
    │   ├── api
    │   └── backend
    ├── client
    │   ├── node_modules
    │   ├── public
    │   └── src
    └── env
    ├── bin
    ├── include
    └── lib

    `cd backend`
    file `settings.py`
    - add (the given url/port is of client/frontend)(this may change)

    `CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173/"
    ]`

    - add/update in `INSTALLED_APPS` section of `settings.py` (to add the packages/installed apps)
    api',
    'corsheaders',
    'rest_framework'

    - add cors middleware in `MIDDLEWAR` section of `settings.py`
        'corsheaders.middleware.CorsMiddleware'

# migrations
python3 manage.py makemigrations
python3 manage.py migrate

# create superuser
python3 manage.py createsuperuser


