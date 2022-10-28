from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import Category, Product,Employee, Order, OrderDetails
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect

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
    context = {
        'order': order,
        'product': product,
        'order_details':order_details
    }
    return render(request, "orders.html", context)


class ProductListView(ListView):
    model = Product
    template_name = "product_list.html"


class ProductDetailView(DetailView):
    model = Product
    template_name = "product_detail.html"

def dummy(request):
    return redirect(reverse_lazy('inventory:order'))







