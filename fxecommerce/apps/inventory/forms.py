from django import forms
from .models import Product, Category, OrderDetails

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'product_name',
            'supplier_id',
            'category_id',
            'quantity_per_unit',
            'unit_price',
            'units_in_stock',
            'units_on_order',
            'reorder_level',
            'discontinued'
        ]

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = [
            'category_name',
            'description',
            'image',
        ]

class OrderDetailsForm(forms.ModelForm):
    class Meta:
        model = OrderDetails
        fields = [
            'product_id',
            'order_id',
            'quantity',
            'discount'
        ]