from django.conf.urls import url, include
from  .views import profile

urlpatterns = [
    url(r'profile/', profile, name='profile'),
]