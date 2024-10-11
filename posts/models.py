from django.db import models
from django.contrib.auth.models import User


# Create your models here.

# Every time you make a model (or make a change to one) use the two commands below:
# python manage.py makemigrations
# python manage.py migrate

class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    thumbnail = models.ImageField(default='default_thumbnail.png', blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.title
    
    def snipped_post(self):
        return self.body[:50] + " (...)"