from django.urls import re_path
from GreetingApp import views
urlpatterns=[
          re_path(r'^$',views.input)
    ]