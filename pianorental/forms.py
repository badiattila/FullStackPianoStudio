from django import forms
from .models import Payment

class MakePaymentForm(forms.Form):

    MONTH_CHOICES = [(i, i) for i in range(1, 12)]
    YEAR_CHOICES = [(i, i) for i in range(2019, 2036)]

    payment_amount = forms.DecimalField(max_digits=5, decimal_places=0, required=True)
    credit_card_number = forms.CharField(label='Credit card number', required=True)
    cvv = forms.CharField(label='Security code (CVV)', required=True)
    expiry_month = forms.ChoiceField(label='Month', choices=MONTH_CHOICES, required=True)
    expiry_year = forms.ChoiceField(label='Year', choices=YEAR_CHOICES, required=True)
    stripe_id = forms.CharField(widget=forms.HiddenInput)
    
class PaymentForm(forms.ModelForm):

    class Meta:
        model = Payment
        fields = ('payment_amount', 'payment_date', 'payment_by')
