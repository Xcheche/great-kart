from django.urls import path
from . import views




urlpatterns = [
    path('cart/',views.cart,name='cart'),
    # path to add to cart
    path('add_to_cart/<int:product_id>/',views.add_to_cart,name='add_to_cart'),
    # Decrease cart view
    path('decrease_cart/<int:product_id>/',views.decrease_cart,name='decrease_cart'),
    # Remove a particular item from the cart
    path('remove_cart/<int:product_id>/',views.remove_cart,name='remove_cart'),
   
]