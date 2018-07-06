from django import forms
from .models import Support


# Форма для отправки сообщения о проблеме на нашу почту
class SupportForm(forms.ModelForm):
    class Meta:
        model = Support
        fields = ('name', 'email', 'comment')
        widgets = {'comment': forms.Textarea(attrs={'cols': 80})}