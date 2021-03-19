from django import forms
from django.forms import ModelForm
from .models import *


class PlayerInfoForm(forms.ModelForm):
    class Meta:
        model = PlayerInfo
        fields = '__all__'
