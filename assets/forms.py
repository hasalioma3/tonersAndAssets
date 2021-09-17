from django.forms import ModelForm
from django import forms
from .models import *


class AssetForm(forms.ModelForm):
    class Meta:
        model = Asset
        fields = ('name', 'barcode', 'serialNumber','accessory')
