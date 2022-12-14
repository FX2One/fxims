from django import forms
from .models import Product #Customer

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


