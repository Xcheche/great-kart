from django.http import HttpResponse
from django.shortcuts import render,redirect

from cart.models import Cart, CartItem
from store.models import Product

# Create your views here.

#--------------Session------------
def _cart_id(request):
    """
    This function retrieves the cart ID from the session.
    If the cart ID does not exist, it creates a new one.
    """
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart









#========Add to Cart View========#
def add_to_cart(request, product_id): # product_id is coming from urls.py
    """
    This function adds a product to the cart.
    """
    product = Product.objects.get(id=product_id)
    try:
        #The cart_id is the session key and we are getting the cart using that cart_id from the Cart model
        cart = Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(
            cart_id = _cart_id(request)
        )
        cart.save()
    try:
        #The product is already in the cart, so we are increasing the quantity
        cart_item = CartItem.objects.get(product=product, cart=cart)
        cart_item.quantity += 1
        cart_item.save()
        
    except CartItem.DoesNotExist:
        #The product is not in the cart, so we are adding it to the cart
        cart_item = CartItem.objects.create(
            #The product is not in the cart, so we are adding it to the cart
            product = product,
            quantity = 1,
            cart = cart
        )
        cart_item.save()
        # for debugging purpose
    # return HttpResponse(cart_item.quantity) 
    # return HttpResponse(cart_item.id) 
    # return HttpResponse(cart_item.product_name) 
    # exit()    
    return redirect('cart')










#========Cart Views========#
def cart(request,total=0,quantity=0,cart_items=None):
    """
    This function retrieves the cart items for a user and calculates the total price and quantity.
    """
    try:
        #Getting the cart using the cart_id from the session _means is private function
        cart = Cart.objects.get(cart_id= _cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart,is_active=True)
        #Calculating the total price and quantity of the cart items
        for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity)
            quantity += cart_item.quantity
    #Tax    choose according to location tax rate or vat     
        tax =(0.075*total)/100
        grand_total = total + tax
    except Exception:
        pass # just ignore    

    context = {
        'total': total,
        'quantity': quantity,
        'cart_items': cart_items,
        'tax':tax,
        'grand_total':grand_total
    }
    return render(request,'cart/cart.html',context)