from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import PianosForRent
from django.contrib.auth.models import User

# Create your views here.

@login_required    
def profile(request, pk=None):
    user = request.user
    try:
        piano = PianosForRent.objects.get(at_user=user)
    except:
        piano = None    
    return render(request, "profile.html", {"piano": piano})    