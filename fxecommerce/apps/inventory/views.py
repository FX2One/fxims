from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Category, Product, Employee, Order, OrderDetails
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import GroupRequiredMixin


class HomeView(TemplateView):
    template_name = "index.html"


class EmployeeListView(GroupRequiredMixin, LoginRequiredMixin, ListView):
    model = Employee
    template_name = "inventory/employees.html"
    context_object_name = 'search_results'
    paginate_by = 10
    group_required = ['ExtraStaff', 'Employee']

    def get_queryset(self):
        search_query = self.request.GET.get('q')
        return Employee.objects.search(search_query)


class EmployeeDetailView(GroupRequiredMixin, LoginRequiredMixin, DetailView):
    model = Employee
    template_name = "inventory/employee_detail.html"
    group_required = ['ExtraStaff', 'Employee']


class CategoryListView(GroupRequiredMixin, LoginRequiredMixin, ListView):
    model = Category
    template_name = "inventory/categories.html"
    paginate_by = 10
    group_required = ['ExtraStaff', 'Employee', 'Customer']

class CategoryCreateView(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    model = Category
    fields = [
        'category_name',
        'description',
        'image',
    ]
    template_name = "inventory/category_create.html"
    success_url = reverse_lazy('inventory:category')
    group_required = ['ExtraStaff', 'Employee']


class OrderDetailsListView(GroupRequiredMixin, LoginRequiredMixin, ListView):
    model = OrderDetails
    template_name = "inventory/orders.html"
    paginate_by = 10
    group_required = ['ExtraStaff', 'Employee', 'Customer']

    def get_queryset(self):
        search_query = self.request.GET.get('q')
        return OrderDetails.objects.search(search_query)


class OrderSpecificationView(GroupRequiredMixin, LoginRequiredMixin, DetailView):
    model = Order
    template_name = "inventory/order_specification.html"
    group_required = ['ExtraStaff', 'Employee']


class ProductListView(GroupRequiredMixin, LoginRequiredMixin, ListView):
    model = Product
    template_name = "inventory/product_list.html"
    paginate_by = 10
    group_required = ['ExtraStaff', 'Employee', 'Customer']

    def get_queryset(self):
        search_query = self.request.GET.get('q')
        return Product.objects.search(search_query)


class ProductDetailView(GroupRequiredMixin, LoginRequiredMixin, DetailView):
    model = Product
    template_name = "inventory/product_detail.html"
    group_required = ['ExtraStaff', 'Employee']


class ProductCreateView(GroupRequiredMixin, LoginRequiredMixin, CreateView):
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
    template_name = "inventory/product_create.html"
    success_url = reverse_lazy('inventory:product_list')
    group_required = ['ExtraStaff', 'Employee']


class ProductUpdateView(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
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
    template_name = "inventory/product_edit.html"
    group_required = ['ExtraStaff', 'Employee']


class ProductDeleteView(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('inventory:product_list')
    template_name = "inventory/product_delete.html"
    group_required = ['ExtraStaff', 'Employee']
