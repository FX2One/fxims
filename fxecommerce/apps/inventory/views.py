from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Category, Product, Employee, Order, OrderDetails
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q



def home(request):
    return render(request, "index.html")


class EmployeeListView(LoginRequiredMixin, ListView):
    model = Employee
    template_name = "employees.html"
    context_object_name = 'search_results'
    paginate_by = 10

    def get_queryset(self):
        search_query = self.request.GET.get('q')
        return Employee.objects.search(search_query)


class EmployeeDetailView(LoginRequiredMixin, DetailView):
    model = Employee
    template_name = "employee_detail.html"


class CategoryListView(LoginRequiredMixin, ListView):
    model = Category
    template_name = "categories.html"
    paginate_by = 10


class OrderDetailsListView(LoginRequiredMixin, ListView):
    model = OrderDetails
    template_name = "orders.html"
    paginate_by = 10

    def get_queryset(self):
        search_query = self.request.GET.get('q')
        return OrderDetails.objects.search(search_query)


class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = "product_list.html"
    paginate_by = 10

    def get_queryset(self):
        search_query = self.request.GET.get('q')
        return Product.objects.search(search_query)


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

