from .models import ShortURL
from django import forms

class CreateNewShortUrl(forms.ModelForm):
    class Meta:
        model = ShortURL
        fields = {'original_url'}

        widgets = {
            'original_url': forms.TextInput(attrs={'class': 'form-control'}),
        }   