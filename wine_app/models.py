from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify

STATUS = ((0, "Draft"), (1, "Published"))


# Create your models here.
class WinePost(models.Model):
    # Use Django's built-in User model for the author
    author = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name="wine_posts"
    )
    
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    wine_name = models.CharField(max_length=100)
    vintage_year = models.IntegerField() 
    content = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.title} | written by {self.author}"

    def save(self, *args, **kwargs):
        # Automatically set the slug from the title if not provided
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        # Updated to match the namespaced URL pattern
        return reverse('wine_app:post_detail', kwargs={'slug': self.slug})


# If you need a custom user profile, create a separate model
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    # Add any additional fields you need for user profiles
    bio = models.TextField(max_length=500, blank=True)
    
    def __str__(self):
        return f"{self.user.username}'s profile"
    
class User(models.Model):
    """
    Custom user model if needed, otherwise use Django's built-in User model.
    """
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)  # Store hashed passwords

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('wine_app:user_profile', kwargs={'username': self.username})