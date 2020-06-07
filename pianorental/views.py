from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import PianosForRent, Payment
from django.contrib.auth.models import User
from datetime import date

# Create your views here.

@login_required    
def profile(request):
    user = request.user
    payments = Payment.objects.all().filter(payment_by = user)
    number_of_payments_made = payments.count() if payments.count() else 0 
    pianos = PianosForRent.objects.all().filter(at_user=user)
    total_days_count = 0
    for piano in pianos:
        # payments_count += (date.today().year - piano.rented_since.year) * 12 + date.today().month - piano.rented_since.month        
        diff = (date.today() - piano.rented_since)
        total_days_count =+ diff.days
    payments_due_count = total_days_count / 30    
    payment_due = True if number_of_payments_made < payments_due_count else False
    return render(request, "profile.html", {"pianos": pianos,"payments": payments, "payment_due": payment_due}) 