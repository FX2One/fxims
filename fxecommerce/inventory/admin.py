from django.contrib import admin
from fxecommerce.inventory.models import Category, Product, Supplier,Order,CustomerDemographics, Customer, Territory, Region, OrderDetails, Shipper, Employee

# Register your models here.
admin.site.register(Employee)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Supplier)
admin.site.register(Customer)
admin.site.register(Shipper)
admin.site.register(Order)
admin.site.register(OrderDetails)
admin.site.register(CustomerDemographics)
admin.site.register(Territory)
admin.site.register(Region)

