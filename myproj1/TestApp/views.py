from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def input(request):
    return HttpResponse("<html><body bgcolor='green' > <h1>Hai! SRAVANI</h1><h2> WELCOME TO DJANGO</h2></body></html>")