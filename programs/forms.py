from django.db import models
from django.forms import ModelForm
from .models import Program

class ProgramForm(ModelForm):
    class Meta:
        model = Program
        fields = ['program', 'username', 'version', 'description', 'date']
        labels = {'program':'Program Name','username':'Authored By'}