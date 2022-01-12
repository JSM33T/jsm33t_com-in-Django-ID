from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

def index(request):   
        return render(request, 'index.html')

def music(request):
        return render(request, 'music/index.html') 
def melancholy(request):
        return render(request, 'music/melancholy/index.html') 
def recuerdos_1(request):
        return render(request, 'music/recuerdos_1/index.html')
def recuerdos_2(request):
        return render(request, 'music/recuerdos_2/index.html')
def recuerdos_3(request):
        return render(request, 'music/recuerdos_3/index.html')

def apps(request):
        return render(request, 'apps/index.html') 
def calc(request):
        return render(request, 'apps/calc/index.html') 

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date = datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!')
    return render(request, 'contact.html')


    



 