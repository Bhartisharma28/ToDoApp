from django import forms
from django.forms import ModelForm
from .models import *
class MyNoteBookModelForm(forms.ModelForm):
    class Meta():
        model=MyNoteBookModel
        fields='__all__'
