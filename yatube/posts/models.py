from django.db import models
from django.contrib.auth import get_user_model
from django.forms import ModelForm

User = get_user_model()
        
class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField("date published", auto_now_add=True)
    author = models.ForeignKey(User, related_name="posts", on_delete=models.CASCADE)
    group = models.ForeignKey('Group', related_name="posts", on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.text

class Group(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    
    def __str__(self):
        return self.title