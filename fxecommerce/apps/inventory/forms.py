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
            'discount',
            'created_by'
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['product_id'].label = 'Select Product'
        self.fields['order_id'].label = 'Order'
        self.fields['quantity'].label = 'Quantity'
        self.fields['discount'].label = 'Discount'
        self.fields['created_by'].label = 'Select Customer to assign Order*'





