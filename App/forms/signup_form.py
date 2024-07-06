from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import ValidationError

class signUpForm(UserCreationForm):
    email = forms.EmailField(max_length=60, required=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Username already exists')
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        user = None
        try:
            user = User.objects.get(email = email)
        except:
            return email
        
        if(user is not None):
            raise forms.ValidationError('Email Already Exists')
        
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
        