from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Published"))


# Create your models here.
class User(models.Model):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)
    
    def __str__(self):
        return self.username
    

class WinePost(models.Model):
    user = models.ForeignKey(
    User, 
    on_delete=models.CASCADE, 
    related_name="wine_posts"
    )

    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
    User, on_delete=models.CASCADE, related_name="blog_posts"
    )

    wine_name = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)
    vintage_year = models.IntegerField() 
    content = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta: # <--- ADD THIS BLOCK
        ordering = ["-created_on"]

    def __str__(self): # <--- ADD THIS METHOD
        return f"{self.title} | written by {self.author}"

