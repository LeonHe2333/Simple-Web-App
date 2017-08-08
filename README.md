# Simple-Web-App
A simple web application(Python)

Use Django(http://djangoproject.com/) to build a project called Learning Log.
Install Django: $ pip install Django

This project works on a virtual enverioment named ll_env.
To install virtual enviroment: $ pip install --user virtualenv
Activate virtual enviroment: $ source ll_env/bin/activate (Linux)
                             $ ll_env\Scripts\activate (Windows)
                             
Creating a project in Django:$ django-admin.py startproject learning_log .

Create the database:$ python manage.py migrate

Start server:$ python manager.py runserver
It works on: http://127.0.0.1:8000/

Start App:$ python manager.py start learning_logs

Modify the database so it can store data of learning_logs:
$ python manage.py makemigragations learning_logs
$ python manage.py migrate

Create superuser: $ python manage.py createsuperuser

