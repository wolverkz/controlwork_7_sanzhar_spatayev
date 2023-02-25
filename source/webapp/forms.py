from django import forms
from .models import Guestbook


class GuestbookForm(forms.ModelForm):
    class Meta:
        model = Guestbook
        fields = ['name', 'email', 'desc']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'desc': forms.Textarea(attrs={'class': 'form-control'}),
        }
