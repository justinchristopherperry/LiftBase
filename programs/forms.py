from django import forms

class ProgramForm(forms.Form):
    username = forms.CharField(max_length=25)
    program = forms.CharField(max_length=50)
    version = forms.IntegerField(required=False)
    description = forms.TextField()
    date = forms.DateTimeField(blank=True, null=True)