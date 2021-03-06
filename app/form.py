from django import forms
from django.forms import fields 
from app.models import *

class NameForm(forms.Form):
    name=forms.CharField(max_length=100)
    mobile=forms.CharField(max_length=10,min_length=10)

class TopicForm(forms.ModelForm):
    class Meta:
        model=Topic
        fields='__all__'