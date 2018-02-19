from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.db.transaction import commit
from lxml.html import clean

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model= User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
            ) 
        
        def save(self, commit=True):
            user = super(RegistrationForm, self).save(commit=False)
            user.first_name = clean['first_name']
            user.last_name = clean['last_name']
            user.email = clean['email']
            
            if commit:
                user.save()
                
            return user
        
class EditProfileForm(UserChangeForm):
    
    class Meta:
        model= User
        fields =(
                'email',
                'first_name',
                'last_name'
#                'password'
            )