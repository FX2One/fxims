from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Category, Product, Employee, Order, OrderDetails
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseRedirect
from django.contrib import messages

def home(request):
    return render(request, "index.html")


class EmployeeListView(UserPassesTestMixin, LoginRequiredMixin, ListView):
    model = Employee
    template_name = "employees.html"
    context_object_name = 'search_results'
    paginate_by = 10
    group_required = ['ExtraStaff', 'Employee']

    def get_queryset(self):
        search_query = self.request.GET.get('q')
        return Employee.objects.search(search_query)


class EmployeeDetailView(UserPassesTestMixin, LoginRequiredMixin, DetailView):
    model = Employee
    template_name = "employee_detail.html"
    group_required = ['ExtraStaff', 'Employee']


class CategoryListView(UserPassesTestMixin, LoginRequiredMixin, ListView):
    model = Category
    template_name = "categories.html"
    paginate_by = 10
    group_required = ['ExtraStaff', 'Employee', 'Customer']


class OrderDetailsListView(UserPassesTestMixin, LoginRequiredMixin, ListView):
    model = OrderDetails
    template_name = "orders.html"
    paginate_by = 10
    group_required = ['ExtraStaff', 'Employee', 'Customer']

    def get_queryset(self):
        search_query = self.request.GET.get('q')
        return OrderDetails.objects.search(search_query)


class OrderSpecificationView(UserPassesTestMixin, LoginRequiredMixin, DetailView):
    model = Order
    template_name = "order_specification.html"
    group_required = ['ExtraStaff', 'Employee']



class ProductListView(UserPassesTestMixin, LoginRequiredMixin, ListView):
    model = Product
    template_name = "product_list.html"
    paginate_by = 10
    group_required = ['ExtraStaff', 'Employee', 'Customer']

    def get_queryset(self):
        search_query = self.request.GET.get('q')
        return Product.objects.search(search_query)

    def test_func(self):
        user = self.request.user
        user_group = user.groups.filter(name__in=self.group_required).exists()
        return user_group or user.is_superuser

    def handle_no_permission(self):
        #if the test_func fails
        messages.warning(self.request, "You do not have rights to access this page")
        return HttpResponseRedirect('/')


class ProductDetailView(UserPassesTestMixin, LoginRequiredMixin, DetailView):
    model = Product
    template_name = "product_detail.html"
    group_required = ['ExtraStaff', 'Employee']

    def test_func(self):
        user = self.request.user
        user_group = user.groups.filter(name__in=self.group_required).exists()
        return user_group or user.is_superuser

    def handle_no_permission(self):
        #if the test_func fails
        messages.warning(self.request, "You do not have rights to access this page")
        return HttpResponseRedirect('/')


class ProductCreateView(UserPassesTestMixin, LoginRequiredMixin, CreateView):
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
    group_required = ['ExtraStaff']


class ProductUpdateView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
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
    group_required = ['ExtraStaff']

class ProductDeleteView(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('inventory:product_list')
    template_name = 'product_delete.html'
    group_required = ['ExtraStaff']

