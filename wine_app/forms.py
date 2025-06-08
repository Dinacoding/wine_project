from django import forms
from .models import WinePost, UserProfile

class WinePostForm(forms.ModelForm):
    class Meta:
        model = WinePost
        fields = ['title', 'wine_name', 'vintage_year', 'content', 'status']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio']