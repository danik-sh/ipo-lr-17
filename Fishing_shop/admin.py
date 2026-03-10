from django.contrib import admin
from .models import Categories, Manufacturer, Product

admin.site.register(Categories)
admin.site.register(Manufacturer)
admin.site.register(Product)