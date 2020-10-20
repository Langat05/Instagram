from django import forms 
from .models import Image, Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(forms.Form):
    email = forms.EmailField(max_length=50, help_text="Required")
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password2')

