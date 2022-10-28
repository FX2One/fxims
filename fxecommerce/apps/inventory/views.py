from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import Category, Product,Employee, Order, OrderDetails
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

def home(request):
    return render(request, "index.html")

@login_required
def employee(request):
    employees = Employee.objects.all()
    return render(request, 'employees.html', {'employees': employees})

@login_required
def product(request):
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})

@login_required
def category(request):
    category = Category.objects.all()
    return render(request, "categories.html", {"category": category})

@login_required
def order(request):
    order = Order.objects.all()
    product = Product.objects.all()
    order_details = OrderDetails.objects.all()
    context = {
        'order': order,
        'product': product,
        'order_details':order_details
    }
    return render(request, "orders.html", context)


class ProductListView(LoginRequiredMixin,ListView):
    model = Product
    template_name = "product_list.html"


class ProductDetailView(LoginRequiredMixin,DetailView):
    model = Product
    template_name = "product_detail.html"








