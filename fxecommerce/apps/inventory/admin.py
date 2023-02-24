from django.contrib import admin
from .models import (Category, Product, Supplier,
                     Order, CustomerDemographics,
                     Territory, Region, OrderDetails,
                     Shipper)


class ProductAdmin(admin.ModelAdmin):
    list_display = ("product_name", "product_id", "units_in_stock", "units_on_order")
    prepopulated_fields = {"slug": ("product_name",)}
    list_per_page = 20


class OrderDetailsAdmin(admin.ModelAdmin):
    list_display = ['order_id', 'product_id', 'quantity', 'discount']

    def save_model(self, request, obj, form, change):
        # If the object is being edited, get the original object from the database
        if change:
            original_obj = OrderDetails.objects.get(pk=obj.pk)
            # Calculate the difference in quantity
            quantity_diff = original_obj.quantity - obj.quantity
            # Update the product's units in stock and units on order fields accordingly
            if quantity_diff > 0:
                # Quantity has been increased, subtract from units_in_stock and add to units_on_order
                obj.product_id.units_in_stock += abs(quantity_diff)
                obj.product_id.units_on_order -= abs(quantity_diff)
            elif quantity_diff < 0:
                # Quantity has been decreased, add to units_in_stock and subtract from units_on_order
                obj.product_id.units_in_stock -= abs(quantity_diff)
                obj.product_id.units_on_order += abs(quantity_diff)
            obj.product_id.save(update_fields=['units_in_stock', 'units_on_order'])
        obj.save()


# Register your models here.
admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(Supplier)
admin.site.register(Shipper)
admin.site.register(Order)
admin.site.register(OrderDetails, OrderDetailsAdmin)
admin.site.register(CustomerDemographics)
admin.site.register(Territory)
admin.site.register(Region)