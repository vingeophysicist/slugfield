from django.db import models
from django.urls import reverse



class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    slug = models.SlugField(max_length=200)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('slugapp:post_detail', args=[self.slug])
    
