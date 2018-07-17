from .models import Index, FAQ
from .models import Contact, Services
from django.shortcuts import render, get_object_or_404


# Create your views here.

def index(request):
    index_elements = Index.objects.all()
    return render(request, 'main_app/index.html', {
        'index_elements': index_elements
    })


def faq(request):
    faq_elements = FAQ.objects.all()
    return render(request, 'main_app/f_a_q.html', {
        'faq_elements': faq_elements
    })


def contacts(request):
    contacts_elements = Contact.objects.all()
    return render(request, 'main_app/contacts.html', {
        'contacts_elements': contacts_elements
    })


def service_list_view(request):
    service_list = Services.objects.all()
    return render(request, 'main_app/services_list.html', {
        'service_list': service_list
    })


def service_detail_view(request, slug):
    service = get_object_or_404(Services, slug=slug, available=True)
    return render(request, 'main_app/services_detail.html', {
        'service': service
    })