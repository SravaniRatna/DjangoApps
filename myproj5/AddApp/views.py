from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def input(request):
    return render(request,"base.html")
    
def compute_sum(request):
    x=int(request.GET['t1'])
    y=int(request.GET['t2'])
    z=x+y
    return HttpResponse("<html><body bgcolor='purple'><h1>SUM="+str(z)+"</h1></body></html>")
