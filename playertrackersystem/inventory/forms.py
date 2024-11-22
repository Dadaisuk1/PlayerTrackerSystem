# forms.py
from django import forms
from .models import inventory

class inventoryForms(forms.ModelForm):
    class Meta:
        model = inventory
        fields = ['item_name', 'item_type', 'cost']
