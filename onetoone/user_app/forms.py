from django import forms
from .models import User, Profile

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        labels = {
            'name' : 'NAME',
            'email' : 'EMAIL'
        }
        widgets ={
            'email' : forms.EmailInput(attrs={
                'class' : 'form-control'
            })
        }

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        labels = {
            'user' : 'USER',
            'bio' : 'BIO'

        }