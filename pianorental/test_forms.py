from django.test import TestCase
from .forms import MakePaymentForm

# Create your tests here.
class TestMakePaymentForm(TestCase):
    def test_can_create_a_payment_form_with_amount_only(self):
        form = MakePaymentForm({'payment_amount' : 20})
        self.assertFalse(form.is_valid())

    # payment_amount = forms.DecimalField(max_digits=5, decimal_places=0, required=True)
    # credit_card_number = forms.CharField(label='Credit card number', required=True)
    # cvv = forms.CharField(label='Security code (CVV)', required=True)
    # expiry_month = forms.ChoiceField(label='Month', choices=MONTH_CHOICES, required=True)
    # expiry_year = forms.ChoiceField(label='Year', choices=YEAR_CHOICES, required=True)
    # stripe_id = forms.CharField(widget=forms.HiddenInput)
    

#     def test_correct_message_for_missing_name(self):
#         form = ItemForm({'name' : ''})
#         self.assertFalse(form.is_valid())
#         self.assertEqual(form.errors['name'], [u'This field is required.'])
        