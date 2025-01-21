
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.forms.widgets import PasswordInput, TextInput



# - CreateUserForm (Model Form)
class CreateUserForm(UserCreationForm):
    
    class Meta:
        
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']
        

# - Authenticate a user (Model Form)

class LoginForm(AuthenticationForm):
    
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())
       

class ContactForm(forms.Form):
    name = forms.CharField(max_length=255)
    email = forms.EmailField()
    mobile_phone = forms.CharField(max_length=255)
    subject = forms.CharField(max_length=255)
    message = forms.CharField(widget=forms.Textarea())













