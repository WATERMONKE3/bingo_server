from django.forms import ModelForm
from django import forms

from .models import *


class BingoForm(forms.Form):
    number = forms.IntegerField()

