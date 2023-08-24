from django.shortcuts import render, HttpResponse
from datetime import datetime
from myapp.models import Contact

def index(request):
    return render(request,"home.html")
def about(request):
    return render(request,"about.html")
    # return HttpResponse("this is about page")
def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        event = request.POST.get("event")
        # print(name,phone,event)
        contact=Contact(name=name,phone=phone,event=event,date=datetime.today())
        contact.save()
    return render(request,"contact.html")
    # return HttpResponse("this is contect page")
def services(request):
    return render(request,"services.html")
    # return HttpResponse("this is inqire page")