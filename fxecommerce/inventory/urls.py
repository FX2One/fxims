from django.urls import path
from . import views
from .views import ProductListView, ProductDetailView

app_name = 'inventory'

urlpatterns = [
    path("products/", ProductListView.as_view(), name="product_list"),
    path("products/<slug:slug>", ProductDetailView.as_view(), name="product_detail"),
    path('employees/', views.employees, name="employees")
]





