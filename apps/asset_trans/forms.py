from django import forms
from django.forms import ModelForm
from .models import *
from .models import Asset_transaction


class Asset_transaction_Form(forms.ModelForm):
    class Meta:
        model = Asset_transaction
        fields = ('user', 'assets', )
