from django.contrib import admin
from .models import Categories, Manufacturer, Product, Bucket, Item_in_bucket

admin.site.register(Categories)
admin.site.register(Manufacturer)
admin.site.register(Product)
admin.site.register(Bucket)
admin.site.register(Item_in_bucket)