from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class BusinessForm(forms.ModelForm):
    class Meta:
        model=Business
        exclude=['user', 'pub_date']


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )

class NewsForm(forms.ModelForm):
    class Meta:
        model=Entry
        exclude=['slug', 'pub_date', 'last_update', 'edited_by']

