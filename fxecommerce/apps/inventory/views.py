from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Category, Product,Employee, Order


def home(request):
    return render(request, "index.html")

def employee(request):
    employees = Employee.objects.all()
    return render(request, 'inventory/employees.html', {'employees': employees})


def product(request):
    products = Product.objects.all()
    return render(request, "inventory/products.html", {"products": products})


def category(request):
    data = Category.objects.all()
    return render(request, "inventory/categories.html", {"data": data})


class ProductListView(ListView):
    model = Product
    template_name = "inventory/product_list.html"


class ProductDetailView(DetailView):
    model = Product
    template_name = "inventory/product_detail.html"




