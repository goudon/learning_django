
## index
tutrial by 
https://docs.djangoproject.com/en/3.1/intro/tutorial01/

## 1. add project
```
# 1. create 
$ django-admin startproject mysite

# 2. build and run 
$ python manage.py runserver

# 3. add app
$ python manage.py startapp polls

# 4. add urls
---
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
---
```

## 2. setting databases

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
## 3. add admin user
```
$ python manage.py createsuperuser
Username (leave blank to use '####'): admin
Email address: admin@example.com   
Password: ####
Password (again): ####
$ python manage.py runserver
```

## 4. polls get edit on admin view
```
# 1. polls on edit (polls/admin.py)
---
from .models import Question
admin.site.register(Question)
---
```

## 5. add views
```
# 1. edit polls view 
---
from django.shortcuts import get_object_or_404, render
from django.http import Http404
from .models import Question

# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)
...
def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

---
# 2. add template (/template/polls/index.html)
---
{{ question.question_text }}
---
# 3. add polls url (/polls/url.py)
---
app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/',views.detail,name='detail'),
    path('<int:question_id>/result',views.results,name='results'),
    path('<int:question_id>/vote/',views.vote,name='vote'),
]
---
# 4. add other views

```



## bigquery

data set:
https://cloud.google.com/bigquery/public-data?hl=ja