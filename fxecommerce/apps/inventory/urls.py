from django.urls import path
from . import views
from .views import (ProductListView, ProductDetailView,
                    ProductCreateView, ProductUpdateView, ProductDeleteView,
                    EmployeeListView, EmployeeDetailView)

app_name = 'inventory'

urlpatterns = [
    path("", views.home, name='home'),
    path("employee/", EmployeeListView.as_view(), name="employee"),
    path("employee/<slug:slug>", EmployeeDetailView.as_view(),name="employee_detail"),
    path("category/", views.category, name="category"),
    path("order/", views.order, name="order"),
    path("products/", ProductListView.as_view(), name="product_list"),
    path("products/create", ProductCreateView.as_view(), name="product_new"),
    path("products/<slug:slug>", ProductDetailView.as_view(), name="product_detail"),
    path("products/<slug:slug>/edit", ProductUpdateView.as_view(), name="product_edit"),
    path("products/<slug:slug>/delete", ProductDeleteView.as_view(), name="product_delete")
]





