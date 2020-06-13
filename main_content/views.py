from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.core.mail import send_mail
from django.utils import timezone
from django.contrib.auth.decorators import login_required, user_passes_test
import urllib, json, os
from urllib import request
from .models import Pianos
from .forms import PianosPostForm

def index(request):
    return render(request, 'index.html')
    
def gallery(request):
    return render(request, 'galery.html')
    
def services(request):
    return render(request, 'services.html')
    
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

def pianos_for_sale(request):
    pianos = Pianos.objects.all()
    return render(request, "pianos_for_sale.html", {"pianos": pianos})

def email_check(user):
    return user.email == 'attila.badi@gmail.com'
    
@login_required    
@user_passes_test(email_check, login_url='index')
def create_or_edit_piano_for_sale(request, pk=None):
    piano = get_object_or_404(Pianos, pk=pk) if pk else None
    if request.method == "POST":
        form = PianosPostForm(request.POST, request.FILES, instance=piano)
        if form.is_valid():
            piano = form.save()
            return redirect(pianos_for_sale)
    else:
        form = PianosPostForm(instance=piano)
    return render(request, 'pianos_for_sale_form.html', {'form': form})

@login_required    
def delete_piano_for_sale(request, pk=None):
    piano = get_object_or_404(Pianos, pk=pk).delete() 
    pianos = Pianos.objects.all()
    return render(request, "pianos_for_sale.html", {"pianos": pianos})