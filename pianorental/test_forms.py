from django.test import TestCase
from .forms import MakePaymentForm

# Create your tests here.
class TestMakePaymentForm(TestCase):
    def test_can_create_a_payment_form_with_amount_only(self):
        form = MakePaymentForm({'payment_amount' : 20})
        self.assertFalse(form.is_valid())

    def test_can_create_a_payment_form_with_amount_and_cardnumber_only(self):
        form = MakePaymentForm({
            'payment_amount' : 20, 
            'credit_card_number' : 4242424242424242
        })
        self.assertFalse(form.is_valid())

    def test_can_create_a_payment_form_with_correct_data(self):
        form = MakePaymentForm({
            'payment_amount' : 20, 
            'credit_card_number' : 4242424242424242,
            'cvv' : 222,
            'expiry_month' : 11,
            'expiry_year' : 2022,
            'stripe_id' : 'secret'
        })
        self.assertTrue(form.is_valid())
