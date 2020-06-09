from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.contrib import messages
from django.conf import settings
from django.utils import timezone
from datetime import date
from .models import PianosForRent, Payment
from .forms import MakePaymentForm, PaymentForm
import stripe, os

stripe.api_key = settings.STRIPE_SECRET
# Create your views here.

@login_required    
def profile(request):
    total_due = 0
    user = request.user
    payments = Payment.objects.all().filter(payment_by = user)
    number_of_payments_made = payments.count() if payments.count() else 0 
    pianos = PianosForRent.objects.all().filter(at_user=user)
    total_days_count = 0
    make_payment_form = MakePaymentForm()    
    payment_form = PaymentForm()
    total_paid = 0
    
    for piano in pianos:
        diff = (date.today() - piano.rented_since)
        total_days_count =+ diff.days
        total_due += (diff.days / 30 * int(piano.price))

    for payment in payments:
        total_paid += payment.payment_amount

    outstanding = int(total_due) - int(total_paid)
    payment_due = True if outstanding > 0 else False
    return render(request, "profile.html", {"pianos": pianos,"payments": payments, "payment_due": payment_due, 'outstanding': outstanding,'total_due': total_due,'total_paid': total_paid, 'make_payment_form': make_payment_form, "publishable": os.getenv('STRIPE_PUBLISHABLE')}) 


@login_required()
def checkout(request):
    if request.method=="POST":
        make_payment_form = MakePaymentForm(request.POST)
        payment_data = Payment()
        if make_payment_form.is_valid():
            total = int(request.POST.get('payment_amount'))
            try:
                customer = stripe.Charge.create(
                    amount = int(total * 100),
                    currency = "EUR",
                    description = request.user.email,
                    card = make_payment_form.cleaned_data['stripe_id'],
                )
            except stripe.error.CardError:
                messages.error(request, "Your card was declined!")
            if customer.paid:
                messages.error(request, "You have successfully paid")
                payment_data.payment_amount = request.POST.get('payment_amount')
                payment_data.payment_date = date.today()
                payment_data.payment_by = request.user
                payment_data.save()
                return redirect(reverse('profile'))
            else:
                messages.error(request, "Unable to take payment")
        else:
            print(make_payment_form.errors)
            messages.error(request, "We were unable to take a payment with that card!")
    else:
        make_payment_form = MakePaymentForm()

    return redirect(reverse('profile'))
