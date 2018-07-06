from django import forms


# Форма для отправки сообщения о проблеме на нашу почту
class SupportForm(forms.Form):
    name = forms.CharField(label='Имя')
    email = forms.EmailField(label='E-mail')
    comment = forms.CharField(label='Комментарий', widget=forms.Textarea)