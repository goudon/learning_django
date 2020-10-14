
## index
tutrial by 
https://docs.djangoproject.com/en/3.1/intro/tutorial01/

## add project
```
# 1. create 
$ django-admin startproject mysite

# 2. build and run 
$ python manage.py runserver

# 3. add app
$ python manage.py startapp polls

# 4. add urls

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
```

## setting databases

```
# 1. migrate
$ python manage.py migrate

# 2. write model (polls/models.py)
add class Question, Choice

# 3. add model in setting as INSTALLED_APPS (mysite/settings.py)
'polls.apps.PollsConfig'

# 4. migrate polls and init polls
$ python manage.py makemigrations polls
$ python manage.py sqlmigrate polls 0001
$ python manage.py migrate

# 5. play on shell
$ python manage.py shell
>>> from polls.models import Choice, Question
>>> Question.objects.all()
>>> from django.utils import timezone
>>> q = Question(question_text="What's new?", pub_date=timezone.now())
>>> q.save()

check 
>>> Question.objects.filter(id=1)
>>> Question.objects.filter(question_text__startswith='What')
```
## add admin user
```
$ python manage.py createsuperuser
Username (leave blank to use '####'): admin
Email address: admin@example.com   
Password: ####
Password (again): ####
$ python manage.py runserver
```

## polls get edit on admin view
```
# 1. polls on edit (polls/admin.py)
from .models import Question
admin.site.register(Question)
```

## bigquery

data set:
https://cloud.google.com/bigquery/public-data?hl=ja