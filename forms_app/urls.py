from django.urls import path
from . import views

urlpatterns = [
    path('support/', views.send_supp, name='support'),
    path('order/', views.send_order, name='order'),
]
