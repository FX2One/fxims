from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Category, Product, Employee, Order, OrderDetails, Customer
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


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
    paginate_by = 2

    def get_paginate_by(self, queryset):
        return self.request.GET.get("paginate_by", self.paginate_by)


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


class ProductUpdateView(LoginRequiredMixin, UpdateView):
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


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('inventory:product_list')
    template_name = 'product_delete.html'


class CustomerCreateView(LoginRequiredMixin, CreateView):
    model = Customer
    fields = ['customer_id''company_name', 'contact_name', 'contact_title', 'address', 'city', 'region', 'postal_code', 'country', 'phone', 'fax']
    template_name = 'customer_create.html'
    success_url = reverse_lazy('inventory:home')
