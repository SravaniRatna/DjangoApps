from django.shortcuts import render

# Create your views here.
def input(request):
    return render(request,"base1.html")

def compute(request):
    pid=int(request.GET["t1"])
    pname = int(request.GET["t2"])
    price = int(request.GET["t3"])
    brand = int(request.GET["t4"])
    qty = int(request.GET["t5"])
    dict={"Proid":pid,"ProName":pname,"ProPrice":price,"ProBrand":brand,"ProQty":qty}
    return render(request,"base2.html",context=dict)
