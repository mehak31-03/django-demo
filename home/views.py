from django.http import HttpResponse
from django.shortcuts import render

from home.models import details 

# Create your views here.
def index(request):
    # return HttpResponse("This is Home page ")
     return render(request,'index.html')

def about(request):
    # return HttpResponse("This is About page ")
     return render(request,'about.html')

def service(request):
    # return HttpResponse("This is Service page ")
     return render(request,'service.html')

def contact(request):
  
     if request.method=="POST":
          name=request.POST.get("name")
          email=request.POST.get("email")
          text=request.POST.get("text")

          print(f"name ={name}, email = {email}, text = {text}")

          contact= details(name=name,email=email,text=text)
          contact.save() 

     return render(request,'contact.html')
