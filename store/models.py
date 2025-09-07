from django.db import models
from category.models import  Category
from django.urls import reverse 
# Create your models here.

#Product models

class Product(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    product_name = models.CharField(max_length=200,unique=True,help_text='Enter product name...')
    slug = models.SlugField(max_length=200,unique=True)
    description = models.TextField(max_length=100,blank=True,help_text='describe the product..') 
    product_images = models.ImageField(upload_to='product_images/%Y/%m/%d/')
    price = models.IntegerField()
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    created_date = models.DateField(auto_now_add=True)
    modified_date = models.DateField(auto_now=True)



    #Get url
    from django.urls import reverse
    def get_absolute_url(self):
        # Canonical URL including category and product slugs
        return reverse('product_detail', kwargs={
            'category_slug': self.category.slug,
            'product_slug': self.slug
        })
    

 
 
    

    
    class Meta:
        verbose_name_plural = "Products"
        indexes = [
            # Creates an index on the 'product_name' field for faster lookups
            models.Index(fields=['product_name']),
            # Creates a composite index on both 'category' and 'price'
            # to speed up queries that filter by both fields
            models.Index(fields=['category', 'price']),
        ]

    def __str__(self):
        return self.product_name # This correctly returns a string    
   
