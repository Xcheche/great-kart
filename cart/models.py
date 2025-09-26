from django.db import models

from store.models import Product

# Create your models here.

#============Cart model================
class Cart(models.Model):
    cart_id = models.CharField(max_length=255,blank=True)
    date_added = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.cart_id} - {self.date_added}'
    
    class Meta:
        verbose_name = "Cart"
        verbose_name_plural = "Carts"



#======Cart Item model================
class CartItem(models.Model):
   
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    is_active  = models.BooleanField(default=True)


    def __str__(self):
        return f'{self.quantity} - {self.is_active}'
    
    class Meta:
        verbose_name = "CartItem"
        verbose_name_plural = "CartItems"
