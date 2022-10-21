from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Category, Product,Employee, Order, OrderDetails


def home(request):
    return render(request, "index.html")

def employee(request):
    employees = Employee.objects.all()
    return render(request, 'employees.html', {'employees': employees})


def product(request):
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})


def category(request):
    category = Category.objects.all()
    return render(request, "categories.html", {"category": category})

def order(request):
    order = Order.objects.all()
    product = Product.objects.all()
    order_details = OrderDetails.objects.all()
    return render(request, "orders.html", {'order': order, 'product':product})


class ProductListView(ListView):
    model = Product
    template_name = "product_list.html"


class ProductDetailView(DetailView):
    model = Product
    template_name = "product_detail.html"




