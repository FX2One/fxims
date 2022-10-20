from django.urls import path
from . import views
from .views import ProductListView, ProductDetailView

app_name = 'inventory'

urlpatterns = [
    path("", views.home, name='home'),
    path("employee/", views.employee, name="employee"),
    path("category/", views.category, name="category"),
    path("products/", ProductListView.as_view(), name="product_list"),
    path("products/<slug:slug>", ProductDetailView.as_view(), name="product_detail"),
]





