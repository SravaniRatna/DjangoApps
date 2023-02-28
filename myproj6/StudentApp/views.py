from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def input(request):
    return render(request,'base.html')

def compute(request):
    stdname=request.GET['t1']
    rollno=int(request.GET['t2'])
    branch=request.GET['t3']
    college=request.GET['t4']
    maths=int(request.GET['t5'])
    physics=int(request.GET['t6'])
    chemistry=int(request.GET['t7'])
    resume=request.GET['t8']
    total=maths+physics+chemistry
    avg=total/3
    return HttpResponse("<html><body bgcolor='yellow' text='red'><h2>STUDENT NAME:"+stdname+
                        "<br>STUDENT ROLLNO:"+str(rollno)+
                        "<br>STUDENT BRANCH:"+branch+
                        "<br>STUDENT COLLEGE:"+college+
                        "<br>MATHS:"+str(maths)+
                        "<br>PHYSICS:"+str(physics)+
                        "<br>CHEMISTRY:"+str(chemistry)+
                        "<br>RESUME:"+resume+
                        "<br>TOTAL MARKS:"+str(total)+
                        "<br>AVERAGE:"+str(avg)+"</h2></body></html>")

