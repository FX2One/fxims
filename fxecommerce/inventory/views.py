from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Category, Product,Employee


def home(request):
    return render(request, "index.html")


'''def products(request):
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})


def categories(request):
    categories = Category.objects.all()
    return render(request, "categories.html", {"categories": categories})'''


class ProductListView(ListView):
    model = Product
    template_name = "inventory/product_list.html"


class ProductDetailView(DetailView):
    model = Product
    template_name = "inventory/product_detail.html"

def employees(request):
    employees = Employee.objects.all()
    return render(request,'employees.html',{'employees':employees})


