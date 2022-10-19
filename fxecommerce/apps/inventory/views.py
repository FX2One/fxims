from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Category, Product,Employee, Order


def home(request):
    return render(request, "index.html")

def employee(request):
    employees = Employee.objects.all()
    return render(request, 'employees.html', {'employees': employees})


def product(request):
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})


def category(request):
    data = Category.objects.all()
    return render(request, "categories.html", {"data": data})


class ProductListView(ListView):
    model = Product
    template_name = "product_list.html"


class ProductDetailView(DetailView):
    model = Product
    template_name = "product_detail.html"




