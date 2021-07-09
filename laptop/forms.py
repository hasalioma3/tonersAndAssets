from django import forms
from django.forms import ModelForm

from .models import Laptop_trans, Department
from assets.models import Asset




class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ('__all__')


class LaptopForm(forms.ModelForm):
    class Meta:
        model = Laptop_trans
        department = forms.ModelChoiceField(queryset=Department.objects.all())
        laptop = forms.ModelChoiceField(queryset=Asset.objects.filter(category=111))
        fields = ('department', 'user', 'laptop', )
