from django.test import TestCase
from .models import PianosForRent, Payment
from django.contrib.auth.models import User
from datetime import date


# Create your tests here

class TestModel(TestCase):
    
    def test_user_with_a_rented_piano(self):
        user = User(
            first_name = "Dirk",
            last_name = "Dirkisson",
            username = "dirkdirkisson",
            email = "dirkdirkisson@dirkisson.com"
            )
        user.save()
        piano = PianosForRent(
            brand = 'Forster',
            price = 23,
            age = 23,
            description = "Some text",
            status = 'o',
            at_user = user,
            rented_since = date.today())
        piano.save()
        self.assertEqual(user.first_name, "Dirk")
        self.assertEqual(str(piano), "Forster")

    def test_user_with_a_payment(self):
        user = User(
            first_name = "Dirk",
            last_name = "Dirkisson",
            username = "dirkdirkisson",
            email = "dirkdirkisson@dirkisson.com"
            )
        user.save()
        payment = Payment(
            payment_amount = 20,
            payment_date = "2020-06-09",
            payment_by = user
            )
        payment.save()
        self.assertEqual(user.email, "dirkdirkisson@dirkisson.com")
        self.assertEqual(str(payment), "Date of payment: 2020-06-09 in amount: EUR 20 .-")

