
from django.contrib import admin
from django.urls import path,re_path
from ProductApp import views

urlpatterns = [
    path("admin/", admin.site.urls),
    re_path(r"^ProductApp$", views.input),
    re_path(r"^comp$", views.compute)

]
