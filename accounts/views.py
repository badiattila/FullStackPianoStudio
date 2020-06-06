from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy, reverse
from django.views import generic
from .forms import UserRegistrationForm
from django.contrib import auth

# We're subclassing the generic class-based view CreateView in our SignUp class. 
# We specify the use of UserRegistrationForm and the template signup.html. 
# And we use reverse_lazy to redirect the user to the login page upon successful registration.

class SignUp(generic.CreateView):
    form_class = UserRegistrationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

