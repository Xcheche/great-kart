from django.db import models
from django.utils.html import format_html

# Create your models here.


# ----------------- Banners--------------------------
class Banner(models.Model):
    banner_img = models.ImageField(upload_to="banners/%Y/%m/%d/")
    alt_text = models.CharField(max_length=150)

    class Meta:
        verbose_name_plural = "Banners"

    def __str__(self):
        return self.alt_text

        # to display image in admin panel

    def image_tag(self):
        return format_html('<img src="{}" width="80" />', self.banner_img.url)