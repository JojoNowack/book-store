from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import fields
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

# new Forms to have the ability to change the username and the profile picture 
class UserUpdateForm(forms.ModelForm):
    
    class Meta: 
        model = User
        fields = ['email']
        
class ProfileUpdateForm(forms.ModelForm):
    
    class Meta: 
        model = Profile
        fields = ['image']