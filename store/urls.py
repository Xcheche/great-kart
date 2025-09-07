from django.urls import path

from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('store/',views.store,name='store'),
    path('<slug:category_slug>/', views.store, name='products_by_category'),
    #Product detail
    path('category/<slug:category_slug>/product/<slug:product_slug>/', views.product_detail, name='product_detail'),

]