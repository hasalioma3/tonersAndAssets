from django import forms
from django.forms import ModelForm
from .models import Toners, Branch

class TonerForm(forms.ModelForm):
    class Meta:
        model = Toners
        branch = forms.ModelChoiceField(queryset=Toners.objects.all())
        fields = ('branch','tonermodels','reading')

class BranchForm(forms.ModelForm):
    class Meta:
        model = Branch
        fields = ('name', 'storeNo')