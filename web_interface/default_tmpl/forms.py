from django import forms
from .models import Default_Templates


#Change path to parent directory for aneasier acces to files
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

from employee.models import Employees


FORMAT_CHOICES = (
    ('pdf', 'PDF'),
    ('docx', 'MS Word'),
)

class DeafaultTemplateForm(forms.ModelForm):
    employee = forms.ModelChoiceField(
        queryset=Employees.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}))
    default_tmpl = forms.ModelChoiceField(
        queryset=Default_Templates.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}))
    format = forms.ChoiceField(choices=FORMAT_CHOICES)

    class Meta:
        model = Employees
        fields = ['employee', 'default_tmpl']