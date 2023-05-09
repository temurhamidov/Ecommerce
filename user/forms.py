from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, UsernameField

from .models import User, Customer

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2',

        ]


class CustomerProfileForms(forms.ModelForm):
    class Meta:
        model = Customer
        fields = [
            'name',
            'locality',
            'city',
            'mobile',
            'state',
            'zipcode',
        ]
        widgets = {
            'name' : forms.TextInput(attrs={'class' : 'form-control'}),
            'locality' : forms.TextInput(attrs={'class' : 'form-control'}),
            'city' : forms.TextInput(attrs={'class' : 'form-control'}),
            'mobile' : forms.NumberInput(attrs={'class' : 'form-control'}),
            'state' : forms.TextInput(attrs={'class' : 'form-control'}),
            'zipcode' : forms.NumberInput(attrs={'class' : 'form-control'}),
        }