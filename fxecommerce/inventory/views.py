from django.shortcuts import render
from .models import Category, Product


def home(request):
    return render(request, "index.html")

def products(request):
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})

def categories(request):
    categories = Category.objects.all()
    return render(request, "categories.html", {"categories": categories})


