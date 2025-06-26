from django.db import models

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    category_image = models.ImageField(upload_to='category_images/%Y/%m/%d/', blank=True, null=True)