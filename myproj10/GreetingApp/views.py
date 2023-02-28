from django.shortcuts import render
import datetime

# Create your views here.
def input(request):
    dt=datetime.datetime.now()
    hour=float(dt.strftime("%H"))
    msg="Hello.....Hyderabad!!!"
    if(hour<=12):
        msg=msg+"Very Good Morning!!!"
    elif(hour<=16.00):
        msg=msg+"Very Good Afternoon!!!"
    elif(hour<=20.00):
        msg=msg+"Very Good Evening!!!"
    else:
        msg=msg+"Very Good Night!!!"
    dict={'message':msg,"date":dt}
    return render(request,'base.html',dict)
