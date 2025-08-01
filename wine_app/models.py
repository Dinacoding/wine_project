# wine_app/models.py

from django.db import models
from django.contrib.auth.models import User # This is Django's built-in User model
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
    content = models.TextField() # Keep as 'content' for the post body
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=1)
    # Adding updated_on is good practice for posts, auto_now=True updates on every save
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        # Using self.author.username for clarity in __str__
        return f"{self.title} | written by {self.author.username}"

    def save(self, *args, **kwargs):
        # Automatically set the slug from the title if not provided
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1
            
            # Keep adding numbers until we find a unique slug
            # Exclude current instance if updating (not creating)
            queryset = WinePost.objects.filter(slug=slug)
            if self.pk:  # If updating existing post
                queryset = queryset.exclude(pk=self.pk)
            
            while queryset.exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
                queryset = WinePost.objects.filter(slug=slug)
                if self.pk:  # If updating existing post
                    queryset = queryset.exclude(pk=self.pk)
            
            self.slug = slug
        super().save(*args, **kwargs)
        

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'slug': self.slug})


# UserProfile model (correct, extends Django's built-in User)
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    bio = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return f"{self.user.username}'s profile"


class Comment(models.Model):
    """
    Model for comments on wine posts.
    """
    post = models.ForeignKey(WinePost, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField() # <--- Changed from 'content' to 'body' for consistency
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        # Ordering comments from oldest to newest (for chronological display)
        # Change to ['-created_on'] if you want newest first
        ordering = ['created_on']

    def __str__(self):
        # Now correctly uses 'self.body'
        return f"Comment {self.body[:50]} by {self.author.username}"