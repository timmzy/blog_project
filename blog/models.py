from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Categories"

class Blog(models.Model):
    title = models.CharField(max_length=100)
    time_stamp = models.DateTimeField(auto_created=True, auto_now_add=True)
    body = models.TextField(max_length=5000)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(null=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('detail', kwargs={'slug': self.slug})

class Comment(models.Model):
    email = models.EmailField(max_length=50)
    name = models.CharField(max_length=50)
    message = models.TextField(max_length=500)
    blog = models.ForeignKey(Blog, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.blog.title
