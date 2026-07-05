from django import forms
from .models import tasks

class Form(forms.ModelForm):
    
    class Meta:
        model = tasks
        fields = ("tittle","detail")

