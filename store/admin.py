from django.contrib import admin
from.models import *
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name','price','modified_date','is_available','category')
    prepopulated_fields = {'slug': ('product_name',)}
    list_editable = ('price','is_available','category')



admin.site.register(Product,ProductAdmin)