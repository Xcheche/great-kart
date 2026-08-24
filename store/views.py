from django.shortcuts import get_object_or_404, render

from cart.models import CartItem
from cart.views import _cart_id
from .models import Product, Category
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.


# Home view
def home(request):
    """
    Render the home page.
    """
    print("Home", "HOME VIEW IS BEING CALLED!")
    products =Product.objects.all().filter(is_available=True)[:3]  # Fetch the first 3 available products
    context = {
        'products':products
    }
    return render(request, 'store/home.html',context)


# Store view with optional category filtering
def store(request, category_slug=None):
    categories = None
    products = None
    print("Store", "STORE VIEW IS BEING CALLED!")
    if category_slug is not None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=categories, is_available=True)
        product_count = products.count()
        paginator = Paginator(products, 1)  # Show 1 product per page
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        
       
    else:
        products = Product.objects.all().filter(is_available=True).order_by('id')
        product_count = products.count()
        paginator = Paginator(products, 1)  # Show 1 product per page
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        print('number of products:', product_count)

    context = {
        'products': paged_products,
        'product_count': product_count,
       
        'page': page
    }
    return render(request, 'store/store.html', context)

# Product detail view
def product_detail(request, category_slug, product_slug):
    in_cart = False
    try:
        single_product = get_object_or_404(
            Product, 
            category__slug=category_slug, 
            slug=product_slug, 
            is_available=True
           
        )

        in_cart = CartItem.objects.filter(
            product=single_product,
            #Cart has a ForeignKey to CartItem model explains the double underscore
            cart__cart_id=_cart_id(request)
        ).exists()
    except Exception as e:
        
        raise e

    context = {
        'single_product': single_product,
        'in_cart': in_cart
    }
    return render(request, 'store/product_detail.html', context)