from django.shortcuts import render
from django.core.mail import send_mail
from .forms import SupportForm


def send_supp(request):
    if request.method == 'POST':
        form = SupportForm(data=request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']  # проверенные данные отправлены в переменную name
            email = form.cleaned_data['email']
            comment = form.cleaned_data['comment']
            # Текст ,отправляемый нам на почту
            data = 'Имя: {0},\n\n Проблема: {1},\n\nE-mail: {2}'.format(name, comment, email)
            send_mail('Support django_web_card', data, name, ['developerspython385@gmail.com'],
                      fail_silently=False)
            first_context = {'name': name}
            return render(request, 'forms_app/thank_for_support.html', first_context)
    form = SupportForm()
    context = {'form': form}
    return render(request, 'forms_app/support.html', context)
