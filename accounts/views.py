from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

# We're subclassing the generic class-based view CreateView in our SignUp class. 
# We specify the use of the built-in UserCreationForm and the template signup.html. 
# And we use reverse_lazy to redirect the user to the login page upon successful registration.

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

