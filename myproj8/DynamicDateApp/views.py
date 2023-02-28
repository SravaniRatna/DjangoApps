from django.shortcuts import render

# Create your views here.
import datetime
def input(request):
    dt=datetime.datetime.now()
    dict1={'date':dt}
    return render(request,'base.html',context=dict1)
