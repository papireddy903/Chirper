from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

from .models import *


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ("email","username")


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ("email","username")


class ChirpForm(forms.ModelForm):
    
    class Meta:
        model = Chirp 
        fields = ['chirp'] 

