from django import forms
from .models import Order, Support


# Форма для отправки сообщения заказчика на нашу почту/базу данных
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('name', 'surname', 'telephone', 'email', 'time', 'service', 'comment', 'flag')
        widgets = {'comment': forms.Textarea(attrs={'cols': 80})}


# Форма для отправки сообщения о проблеме на нашу почту/базу данных
class SupportForm(forms.ModelForm):
    class Meta:
        model = Support
        fields = ('name', 'email', 'comment')
        widgets = {'comment': forms.Textarea(attrs={'cols': 80})}
