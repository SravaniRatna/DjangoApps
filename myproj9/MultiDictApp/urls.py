from django.urls import re_path
from MultiDictApp import views
urlpatterns=[
      re_path(r'^$',views.input)
]