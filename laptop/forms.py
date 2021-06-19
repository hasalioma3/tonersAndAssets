from django import forms
from django.forms import ModelForm

from .models import Laptop,Laptopmodel, Department

class LaptopmodelForm(forms.ModelForm):
    class Meta:
        model = Laptopmodel
        fields = ('__all__')

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ('__all__')


class LaptopForm(forms.ModelForm):
    class Meta:
        model = Laptop
        department = forms.ModelChoiceField(queryset=Department.objects.all())
        laptopmodel = forms.ModelChoiceField(queryset=Laptopmodel.objects.all())
        fields = ('department', 'laptopmodel', 'user', 'serialno', 'barcode')

