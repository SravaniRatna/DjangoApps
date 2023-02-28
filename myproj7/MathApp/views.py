from django.shortcuts import render
import math

# Create your views here.
def input(request):
    return render(request,'base1.html')

def compute(request):
    x=int(request.GET['t1'])
    dict1={'res':math.sqrt(x)}
    return render(request,'base2.html',context=dict1)
    