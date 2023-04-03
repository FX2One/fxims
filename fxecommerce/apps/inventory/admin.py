from django.contrib import admin
from .models import (Category, Product, Supplier,
                     Order, CustomerDemographics,
                     Territory, Region, OrderDetails,
                     Shipper)

from users.models import User
from inventory.forms import OrderDetailsForm


class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'product_id', 'units_in_stock', 'units_on_order','reorder_level')
    prepopulated_fields = {'slug': ('product_name',)}
    list_per_page = 20


class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_id','ship_via','order_status',)
    exclude = ('freight',)

    # turn off Order creation
    # Order is auto-created via OrderDetails model and connected signals
    def has_add_permission(self, request, obj=None):
        if request.user.is_superuser:
            return False
        return super().has_add_permission(request)

class ShipperAdmin(admin.ModelAdmin):
    list_display = ('company_name','freight_price')


class OrderDetailsAdmin(admin.ModelAdmin):
    list_display = ['order_id', 'product_id', 'quantity', 'discount', 'total_amount','discounted_total','total_price']
    exclude = ('order_id','unit_price','total_amount','discounted_total','total_price')

    form = OrderDetailsForm


    def get_readonly_fields(self, request, obj=None):
        if obj:  # If obj is not None, it means the object is being edited
            return ['product_id', 'order_id']  # Make field1 and field2 read-only
        else:  # If obj is None, it means the object is being added
            return []

    # limit created_by only to user_type=4
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "created_by":
            kwargs["queryset"] = User.objects.filter(user_type=4)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

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
admin.site.register(Shipper, ShipperAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderDetails, OrderDetailsAdmin)
admin.site.register(CustomerDemographics)
admin.site.register(Territory)
admin.site.register(Region)