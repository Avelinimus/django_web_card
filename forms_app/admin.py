from django.contrib import admin
from .models import Support, Order


@admin.register(Support)
class SupportAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'comment']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname', 'telephone', 'email', 'time', 'service', 'comment']
