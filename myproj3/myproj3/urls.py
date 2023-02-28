
from django.contrib import admin
from django.urls import path,re_path
from MultiViewApp import views

urlpatterns = [
    path("admin/", admin.site.urls),
    re_path(r'^emp$',views.emp),
    re_path(r'^cust$',views.cust),
]
