# from django import forms
# class ProgramForm(forms.Form):
#     username = forms.CharField(max_length=25)
#     program = forms.CharField(max_length=50)
#     version = forms.IntegerField(required=False)
#     description = forms.CharField(max_length=500)
#     date = forms.DateTimeField(required=False)

from django.db import models
from django.forms import ModelForm
from .models import Program
class ProgramForm(ModelForm):
    class Meta:
        model = Program
        fields = ['username', 'program', 'version', 'description', 'date']