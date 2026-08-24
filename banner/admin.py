from django.contrib import admin
from .models import Banner
# Register your models here.


class BannerAdmin(admin.ModelAdmin):
    list_display = ('alt_text', 'image_tag','banner_img')  # Display alt_text and image_tag in the admin list view
    readonly_fields = ('image_tag',)  # Make image_tag read-only in the admin form
    list_editable = ('banner_img',)  # Allow editing of banner_img in the admin list view


admin.site.register(Banner, BannerAdmin)  # Register the Banner model with the custom admin class    