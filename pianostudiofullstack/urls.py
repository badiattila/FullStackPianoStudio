"""pianostudiofullstack URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from main_content.views import index, gallery, services, rent, contact, contact_send, pianos_for_sale, create_or_edit_piano_for_sale, delete_piano_for_sale
from django.urls import path 

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')), 
    path('accounts/', include('accounts.urls')),
    path('pianorental/', include('pianorental.urls')),     
    url(r'^$', index, name='index'),
    url(r'^services/', services, name='services'),
    url(r'^rent/', rent, name='rent'),
    url(r'^createadd/', index, name='createadd'),
    url(r'^pianos_for_sale/', pianos_for_sale, name='pianos_for_sale'),
    url(r'^gallery/', gallery, name='gallery'),
    url(r'^contact/', contact, name='contact'),
    url(r'^contact_send/', contact_send, name='contact_send'),
    url(r'^new_piano_post/', create_or_edit_piano_for_sale, name='new_piano_post'),
    url(r'^(?P<pk>\d+)/edit_piano/$', create_or_edit_piano_for_sale, name='create_or_edit_piano_for_sale'),
    url(r'^(?P<pk>\d+)/delete_piano/$', delete_piano_for_sale, name='delete_piano_for_sale'),
]
