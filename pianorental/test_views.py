from django.test import TestCase
from django.shortcuts import get_object_or_404
from .models import PianosForRent, Payment
from django.contrib.auth.models import User


# Create your tests here.
class TestViews(TestCase):
    def setUp(self):
        self.credentials = {
            'username': 'testuser',
            'password': 'secret'}
        User.objects.create_user(**self.credentials)
    def test_login(self):
        # send login data
        response = self.client.post('/accounts/login/', self.credentials, follow=True)
        # should be logged in now
        self.assertTrue(response.context['user'].is_active)

    def test_user_with_piano(self):
        piano = PianosForRent(
            brand = 'Forster',
            price = 23,
            age = 23,
            description = "Some text",
            status = 'o',
            at_user = User.objects.get_by_natural_key('testuser') ,
            rented_since = "2020-06-09")
        piano.save()        
        response = self.client.post('/accounts/login/', self.credentials, follow=True)
        self.assertTrue(response.context['user'].is_active)
        
    def test_user_with_piano_and_payment(self):
        piano = PianosForRent(
            brand = 'Forster',
            price = 23,
            age = 23,
            description = "Some text",
            status = 'o',
            at_user = User.objects.get_by_natural_key('testuser') ,
            rented_since = "2020-06-09")
        piano.save()
        payment = Payment(
            payment_amount = 200,
            payment_date = "2020-06-09",
            payment_by = User.objects.get_by_natural_key('testuser')
            )
        payment.save()        
        response = self.client.post('/accounts/login/', self.credentials, follow=True)
        self.assertTrue(response.context['user'].is_active)
        
