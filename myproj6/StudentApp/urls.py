from django.urls import re_path
from StudentApp import views #or from . import views
urlpatterns=[
          re_path(r'^$',views.input),
          re_path(r'^comp$',views.compute)
          ]
