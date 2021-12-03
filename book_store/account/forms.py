from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

# falls eine Profil-Änderung gebraucht wird:
class UserUpdateForm(forms.ModelForm):
        # email = forms.EmailField()
    
        class Meta:
            model = User
            fields = ['username']
 
# Änderungen für das Profil -> jeder User kann sein Profilbild           
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
        
