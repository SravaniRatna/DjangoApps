from django.urls import re_path
from TestApp import views
urlpatterns = [
    re_path(r'^input$',views.input)
    
]
