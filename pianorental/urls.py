from django.conf.urls import url, include
from  .views import profile, checkout, rent

urlpatterns = [
    url(r'profile/', profile, name='profile'),
    url(r'checkout/', checkout, name='checkout'),
    url(r'rent/', rent, name='rent'),
]
