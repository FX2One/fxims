from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Category, Product, Order, OrderDetails
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import GroupRequiredMixin
from .forms import OrderDetailsForm, ProductForm, CategoryForm
from django import forms


class HomeView(TemplateView):
    template_name = "index.html"



class CategoryListView(GroupRequiredMixin, LoginRequiredMixin, ListView):
    model = Category
    template_name = "inventory/categories.html"
    paginate_by = 10
    group_required = ['ExtraStaff', 'Employee', 'Customer']

    def get_paginate_by(self, queryset):
        return self.request.GET.get("paginate_by", self.paginate_by)

class CategoryCreateView(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    model = Category
    template_name = "inventory/category_create.html"
    success_url = reverse_lazy('inventory:category')
    form_class = CategoryForm
    group_required = ['ExtraStaff', 'Employee']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        return context

class OrderDetailsListView(GroupRequiredMixin, LoginRequiredMixin, ListView):
    model = OrderDetails
    template_name = "inventory/orders.html"
    paginate_by = 10
    group_required = ['ExtraStaff', 'Employee', 'Customer']


    def get_queryset(self):
        search_query = self.request.GET.get('q')
        user_type = self.request.user.user_type

        if user_type == 4:
            # If user_type is 4, only show OrderDetails created by the current user
            return OrderDetails.objects.filter(created_by=self.request.user).exclude(created_by=None).search(search_query)
        else:
            # Otherwise if user_type == 1, show all OrderDetails
            return OrderDetails.objects.search(search_query)

    def get_paginate_by(self, queryset):
        return self.request.GET.get("paginate_by", self.paginate_by)


class OrderDetailsCreateView(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    model = OrderDetails
    template_name = "inventory/orders_create.html"
    success_url = reverse_lazy('inventory:order')
    form_class = OrderDetailsForm
    paginate_by = 10
    group_required = ['ExtraStaff', 'Employee', 'Customer']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        return context

    def form_valid(self, form):
        # check if created_by field is set in the form data
        created_by = form.cleaned_data.get('created_by', None)
        if created_by:
            form.instance.created_by = created_by
        else:
            form.instance.created_by = self.request.user

        return super().form_valid(form)


class OrderDetailsUpdateView(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    model = OrderDetails
    template_name = "inventory/orders_edit.html"
    success_url = reverse_lazy('inventory:order')
    form_class = OrderDetailsForm
    group_required = ['ExtraStaff', 'Employee', 'Customer']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        return context


class OrderDetailsDeleteView(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('inventory:orders')
    template_name = "inventory/orders_delete.html"
    group_required = ['ExtraStaff', 'Employee', 'Customer']


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

    def get_paginate_by(self, queryset):
        return self.request.GET.get("paginate_by", self.paginate_by)


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
    success_url = reverse_lazy('inventory:product_list')
    template_name = "inventory/product_edit.html"
    form_class = ProductForm
    group_required = ['ExtraStaff', 'Employee']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        return context


class ProductDeleteView(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('inventory:product_list')
    template_name = "inventory/product_delete.html"
    group_required = ['ExtraStaff', 'Employee']
