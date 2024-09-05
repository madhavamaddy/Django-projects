from django import forms
from .models import Navals

class ItemForm(forms.ModelForm):
    class Meta:
        model = Navals
        fields = ['name', 'description']
