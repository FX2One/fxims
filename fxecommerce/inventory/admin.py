from django.contrib import admin
from fxecommerce.inventory.models import Category, Product, Supplier

# Register your models here.

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Supplier)
