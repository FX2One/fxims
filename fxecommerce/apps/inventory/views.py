from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Category, Product, Employee, Order, OrderDetails
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ProductForm


def home(request):
    return render(request, "index.html")


class EmployeeListView(LoginRequiredMixin, ListView):
    model = Employee
    template_name = "employees.html"

class EmployeeDetailView(LoginRequiredMixin, DetailView):
    model = Employee
    template_name = "employee_detail.html"



@login_required
def category(request):
    category = Category.objects.all()
    context = {
        'category': category
    }
    return render(request, "categories.html", context)


@login_required
def order(request):
    order = Order.objects.all()
    product = Product.objects.all()
    order_details = OrderDetails.objects.all()
    context = {
        'order': order,
        'product': product,
        'order_details': order_details
    }
    return render(request, "orders.html", context)


class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = "product_list.html"

    '''def get_context_data(self, **kwargs):
        context = super(ProductListView,self).get_context_data(**kwargs)
        context['form'] = ProductForm()
        return context'''


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = "product_detail.html"


class ProductCreateView(LoginRequiredMixin, CreateView):
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
    template_name = 'product_create.html'
    success_url = reverse_lazy('inventory:product_list')


class ProductUpdateView(UpdateView):
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
    success_url = reverse_lazy('inventory:product_list')
    template_name = 'product_edit.html'


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('inventory:product_list')
    template_name = 'product_delete.html'
