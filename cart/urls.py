from django.urls import path
from . import views




urlpatterns = [
    path('cart/',views.cart,name='cart'),
    # path to add to cart
    path('add_to_cart/<int:product_id>/',views.add_to_cart,name='add_to_cart'),
    # path to remove cart item
   
]