from django.test import TestCase
from django.shortcuts import get_object_or_404, reverse
from django.contrib.auth.models import User
from .models import PianosForRent, Payment
from .forms import MakePaymentForm
import datetime

# Create your tests here.
class TestViews(TestCase):
    def setUp(self):
        self.credentials = {
            'username': 'testuser',
            'password': 'secret',
            'first_name': 'Some',
            'last_name': 'Dude',
            'email': 'some@dude.ie'
        }
        User.objects.create_user(**self.credentials)
      
    def test_rent(self):
        piano = PianosForRent(
            brand = 'Forster',
            price = 23,
            age = 23,
            description = "Some text",
            status = 'a',
            at_user = User.objects.get_by_natural_key('testuser') ,
            rented_since = datetime.date.today() - datetime.timedelta(weeks=12))
        piano.save()        
        response = self.client.get('/pianorental/rent/', follow=True)
        self.assertEqual(response.context['pianos'].count(), 1)
        self.assertEqual(response.status_code, 200)

    def test_login(self):
        # send login data
        response = self.client.post('/accounts/login/', self.credentials, follow=True)
        # should be logged in now
        self.assertTrue(response.context['user'].is_active)
        self.assertEqual(response.status_code, 200)
        
    def test_user_with_piano(self):
        piano = PianosForRent(
            brand = 'Forster',
            price = 23,
            age = 23,
            description = "Some text",
            status = 'o',
            at_user = User.objects.get_by_natural_key('testuser') ,
            rented_since = datetime.date.today() - datetime.timedelta(weeks=12))
        piano.save()        
        response = self.client.post('/accounts/login/', self.credentials, follow=True)
        self.assertTrue(response.context['user'].is_active)
        self.assertEqual(response.context['pianos'].count(), 1)
        self.assertEqual(response.status_code, 200)
        
    def test_user_with_piano_and_insufficient_payment(self):
        piano = PianosForRent(
            brand = 'Forster',
            price = 23,
            age = 23,
            description = "Some text",
            status = 'o',
            at_user = User.objects.get_by_natural_key('testuser') ,
            rented_since = datetime.date.today() - datetime.timedelta(weeks=12))
        piano.save()
        payment = Payment(
            payment_amount = 2,
            payment_date = "2020-05-09",
            payment_by = User.objects.get_by_natural_key('testuser')
            )
        payment.save()
        response = self.client.post('/accounts/login/', self.credentials, follow=True)
        self.assertTrue(response.context['user'].is_active)
        self.assertEqual(response.context['payments'].count(), 1)
        self.assertEqual(response.context['payments'][0].payment_amount, 2)
        self.assertTrue(response.context['payment_due'])
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['outstanding'], 67)
        self.assertEqual(response.context['total_due'], 69)
        self.assertEqual(response.context['total_paid'], 2)
        self.assertFalse(response.context['make_payment_form'].is_valid())

    def test_user_with_piano_and_no_payment(self):
        piano = PianosForRent(
            brand = 'Forster',
            price = 23,
            age = 23,
            description = "Some text",
            status = 'o',
            at_user = User.objects.get_by_natural_key('testuser') ,
            rented_since = datetime.date.today() - datetime.timedelta(weeks=12))
        piano.save()
        response = self.client.post('/accounts/login/', self.credentials, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['user'].is_active)
        self.assertEqual(response.context['user'].username, 'testuser')
        self.assertEqual(response.context['pianos'][0].brand, 'Forster')
        self.assertEqual(response.context['payments'].count(), 0)
        self.assertEqual(response.context['outstanding'], 69)
        self.assertEqual(response.context['total_due'], 69)
        self.assertEqual(response.context['total_paid'], 0)   
        
    def test_user_with_piano_and_sufficient_payment(self):
        piano = PianosForRent(
            brand = 'Forster',
            price = 23,
            age = 23,
            description = "Some text",
            status = 'o',
            at_user = User.objects.get_by_natural_key('testuser') ,
            rented_since = datetime.date.today() - datetime.timedelta(weeks=12))
        piano.save()
        payment = Payment(
            payment_amount = 2000,
            payment_date = "2020-05-09",
            payment_by = User.objects.get_by_natural_key('testuser')
            )
        payment.save()        
        response = self.client.post('/accounts/login/', self.credentials, follow=True)
        self.assertTrue(response.context['user'].is_active)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.context['payment_due'])
        self.assertEqual(response.context['outstanding'], -1931)
        self.assertEqual(response.context['total_due'], 69)
        self.assertEqual(response.context['total_paid'], 2000)        
        
    def test_checkout_payment_successful(self):
        piano = PianosForRent(
            brand = 'Forster',
            price = 23,
            age = 23,
            description = "Some text",
            status = 'a',
            at_user = User.objects.get_by_natural_key('testuser') ,
            rented_since = datetime.date.today() - datetime.timedelta(weeks=12))
        piano.save()        
        response = self.client.post('/accounts/login/', self.credentials, follow=True)
        self.assertEqual(response.context['pianos'].count(), 1)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['payment_due'])
        self.assertEqual(response.context['outstanding'], 69)
        self.assertEqual(response.context['total_due'], 69)
        self.assertEqual(response.context['total_paid'], 0)           
        response2 = self.client.post('/pianorental/checkout/', {
            'payment_amount' : 2000, 
            'credit_card_number' : 4242424242424242, 
            'cvv' : 222, 
            'expiry_month' : 11, 
            'expiry_year' : 2022,
            'stripe_id': 'tok_us'}, follow=True)
        self.assertFalse(response2.context['payment_due'])

        