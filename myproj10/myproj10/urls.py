
from django.contrib import admin
from django.urls import path,re_path
from django.conf.urls import url,include
urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^www.Greeting.com/', include('GreetingApp.urls')),
    re_path(r'^www.Greeting.com/', include('GreetingApp.urls'))
]
