from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.index, name='index'),
    path('services', views.services, name='services'),
    path('faq', views.faq, name='faq'),
    path('contacts', views.contacts, name='contacts'),
]