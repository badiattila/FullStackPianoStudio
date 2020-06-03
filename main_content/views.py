from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.core.mail import send_mail
import urllib, json, os
from urllib import request

def index(request):
    return render(request, 'index.html')
    
def gallery(request):
    return render(request, 'galery.html')
    
def services(request):
    return render(request, 'services.html')

def rent(request):
    return render(request, 'rent.html')
    
def contact(request):
    return render(request, 'contact.html')
    
def contact_send(request):
    try:
        send_mail(
            "Contact from pianostudio (" + request.POST.get('user_fname') +" "+ request.POST.get('user_sname') +")",
            request.POST.get('message'),
            request.POST.get('user_email'),
            ['attila.badi@gmail.com'],
            fail_silently=False,
        )
        return render(request, 'contact_success.html')
    except:
        return render(request, 'contact_error.html')    
    return render(request, 'contact.html')
