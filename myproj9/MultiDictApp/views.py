from django.shortcuts import render
import datetime

# Create your views here.
def input(request):
    date=datetime.datetime.now()
    day=date.strftime("%A")
    month=date.strftime("%B")
    year=date.strftime("%Y")
    dict={'date':date,'cur_day':day,'cur_month':month,'cur_year':year}
    return render(request,'base.html',context=dict)
