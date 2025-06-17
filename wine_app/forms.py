from django import forms
from .models import WinePost, UserProfile   
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User   

class WinePostForm(forms.ModelForm):
    class Meta:
        model = WinePost
        fields = ['title', 'wine_name', 'vintage_year', 'content', 'status']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio']
        

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
