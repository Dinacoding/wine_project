from django import forms
from .models import WinePost, UserProfile, Comment 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User   

class WinePostForm(forms.ModelForm):
    class Meta:
        model = WinePost
        fields = ['title', 'wine_name', 'vintage_year', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter post title'}),
            'wine_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter wine name'}),
            'vintage_year': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'e.g. 2015'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Write your post here...'}),
        }

class winePostEditForm(forms.ModelForm):
    class Meta:
        model = WinePost
        fields = ['title', 'wine_name', 'vintage_year', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter post title'}),
            'wine_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter wine name'}),
            'vintage_year': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'e.g. 2015'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Update your post here...'}),
        }

class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter first name'
        })
    )
    last_name = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter last name'
        })
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter email'
        })
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter username'
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add styling to password fields
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control w-100',
            'placeholder': 'Enter password'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control w-100',
            'placeholder': 'Confirm password'
        })

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
        return user

