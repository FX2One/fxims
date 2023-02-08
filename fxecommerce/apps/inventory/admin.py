from django.contrib import admin
from .models import (Category, Product, Supplier,
                     Order, CustomerDemographics,
                     Territory, Region, OrderDetails,
                     Shipper)


class ProductAdmin(admin.ModelAdmin):
    list_display = ("product_name", "product_id")
    prepopulated_fields = {"slug": ("product_name",)}
    list_per_page = 20


# Register your models here.
admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(Supplier)
admin.site.register(Shipper)
admin.site.register(Order)
admin.site.register(OrderDetails)
admin.site.register(CustomerDemographics)
admin.site.register(Territory)
admin.site.register(Region)