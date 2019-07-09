from django.db import models
from django.forms import ModelForm

class Program(models.Model):
    username = models.CharField(max_length=25)
    program = models.CharField(max_length=50)
    version = models.IntegerField(blank=True, null=True)
    description = models.TextField()
    date = models.DateTimeField(blank=True, null=True)

class ProgramForm(ModelForm):
    class Meta:
        model = Program
        fields = ['username', 'program', 'version', 'description', 'date']


