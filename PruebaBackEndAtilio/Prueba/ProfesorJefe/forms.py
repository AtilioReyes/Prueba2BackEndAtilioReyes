from django import forms
from django.core import validators
from ProfesorJefe.models import ProfJefe

class FormProfeJefe(forms.ModelForm):
    class Meta: 
        model = ProfJefe
        fields = '__all__'