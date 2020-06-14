from django.test import TestCase
from .forms import UserRegistrationForm
from django.contrib.auth.models import User

# Create your tests here.
class TestUserRegistrationForm(TestCase):
    def setUp(self):
        self.credentials = {
            'username': 'testuser',
            'password': 'secret',
            'first_name': 'Some',
            'last_name': 'Dude',
            'email': 'some@dude.ie'
        }
        User.objects.create_user(**self.credentials)
      
    def test_can_create_a_registration_form_with_correct_values(self):
        form = UserRegistrationForm({
            'password1' : "SecretPass",
            'password2' : "SecretPass",
            'first_name' : "First",
            'last_name' : "Last",
            'username' : "someuser",
            'email' : "some@mail.com",
        })
        self.assertTrue(form.is_valid())

    def test_can_create_a_registration_form_with_not_matching_pw(self):
        form = UserRegistrationForm({
            'password1' : "SecretPass",
            'password2' : "SecretOtherPass",
            'first_name' : "First",
            'last_name' : "Last",
            'username' : "someuser",
            'email' : "some@mail.com",
        })
        self.assertFalse(form.is_valid())

    def test_can_create_a_registration_form_with_empty_pw(self):
        form = UserRegistrationForm({
            'password1' : "",
            'password2' : "SecretPass",
            'first_name' : "First",
            'last_name' : "Last",
            'username' : "someuser",
            'email' : "some@mail.com",
        })
        self.assertFalse(form.is_valid())

    def test_can_create_a_registration_form_with_existing_email(self):
        form = UserRegistrationForm({
            'password1' : "SecretPass",
            'password2' : "SecretPass",
            'first_name' : "First",
            'last_name' : "Last",
            'username' : "someuser",
            'email' : "some@dude.ie",
        })
        self.assertFalse(form.is_valid())
