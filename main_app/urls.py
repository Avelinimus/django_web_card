from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.index, name='index'),
    path('faq', views.faq, name='faq'),
    path('contacts', views.contacts, name='contacts'),
]

urlpatterns += [
    path('services', views.service_list_view, name='service_list'),
    url(r'^service/(?P<slug>[\w-]+)/$', views.service_detail_view, name='service_detail'),
]