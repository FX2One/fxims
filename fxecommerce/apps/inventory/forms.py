from django import forms
from .models import Product, Category, OrderDetails
from django.core.exceptions import ValidationError
from users.models import User

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
    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['product_id'].label = 'Select Product'
        self.fields['order_id'].label = 'Order'
        self.fields['quantity'].label = 'Quantity'
        self.fields['discount'].label = 'Discount'
        self.fields['created_by'].label = 'Select Customer to assign Order*'

        if user and user.user_type == 4:
            self.fields['created_by'].queryset = User.objects.filter(id=user.id)
            self.fields['created_by'].initial = user
            self.fields['created_by'].disabled = True
        else:
            self.fields['created_by'].queryset = User.objects.filter(user_type=4)

    def clean_created_by(self):
        created_by = self.cleaned_data.get('created_by', None)
        if not created_by:
            raise forms.ValidationError('Please select a customer.')
        return created_by

    class Meta:
        model = OrderDetails
        fields = [
            'product_id',
            'order_id',
            'unit_price',
            'quantity',
            'discount',
            'created_by',
            'total_amount',
            'discounted_total',
            'total_price',
        ]










