from django.shortcuts import render
from django.core.mail import send_mail
from .forms import SupportForm, OrderForm


def send_order(request):
    if request.method == 'POST':
        form = OrderForm(data=request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            surname = form.cleaned_data['surname']
            telephone = form.cleaned_data['telephone']
            email = form.cleaned_data['email']
            time = form.cleaned_data['time']
            comment = form.cleaned_data['comment']
            flag = form.cleaned_data['flag']
            data = ' Имя: {0} {1}, \n\n ' \
                   'Мобильный телефон: {2}, \n\n ' \
                   'E-mail: {3}, \n\n ' \
                   'Удобное время: {4}, \n\n ' \
                   'Комментарий: {5}'.format(name, surname, telephone, email, time, comment)
            send_mail('Заказ',
                      data,
                      email,
                      ['developerspython385@gmail.com'],
                      fail_silently=False)
            if flag:
                send_mail('Заказ принят',
                          'Ваши данные:\n\n' + data,
                          'developerspython385@gmail.com',
                          [email],
                          fail_silently=False)
            form.save(commit=False)
            form.save()
            return render(request, 'forms_app/successful_order.html', {'name': name, 'surname': surname})
    else:
        form = OrderForm()
    return render(request, 'forms_app/order.html', {'form': form})


def send_supp(request):
    if request.method == 'POST':
        form = SupportForm(data=request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']  # проверенные данные отправлены в переменную name
            email = form.cleaned_data['email']
            comment = form.cleaned_data['comment']
            # Текст ,отправляемый нам на почту
            data = 'Имя: {0},\n\n Проблема: {1},\n\nE-mail: {2}'.format(name, comment, email)
            send_mail('Support django_web_card',
                      data,
                      name,
                      ['developerspython385@gmail.com'],
                      fail_silently=False)
            form.save(commit=False)
            form.save()
            return render(request, 'forms_app/successful_support.html', {'name': name})
    else:
        form = SupportForm()
    return render(request, 'forms_app/support.html', {'form': form})
