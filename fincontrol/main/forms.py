from django import forms
from .models import *

class transaction_form(forms.ModelForm):
    class Meta:
        model = transaction
        fields = '__all__'

