from django.conf.urls import url, include
from .views import gallery, services, contact, contact_send, pianos_for_sale

urlpatterns = [
    url(r'services/', services, name='services'),
    url(r'pianos_for_sale/', pianos_for_sale, name='pianos_for_sale'),
    url(r'gallery/', gallery, name='gallery'),
    url(r'contact/', contact, name='contact'),
    url(r'contact_send/', contact_send, name='contact_send')
    ]