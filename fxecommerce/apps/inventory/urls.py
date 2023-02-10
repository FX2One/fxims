from django.urls import path
from . import views
from .views import (ProductListView, ProductDetailView,
                    ProductCreateView, ProductUpdateView, ProductDeleteView,
                    OrderDetailsListView,
                    OrderSpecificationView, CategoryListView, CategoryCreateView, HomeView)

app_name = 'inventory'


urlpatterns = [
    path("", HomeView.as_view(), name='home'),

    path("category/", CategoryListView.as_view(), name="category"),
    path("category/create", CategoryCreateView.as_view(), name="category_new"),
    path("order/", OrderDetailsListView.as_view(), name="order"),
    path("order/<int:pk>", OrderSpecificationView.as_view(), name="order_detail"),
    path("products/", ProductListView.as_view(), name="product_list"),
    path("products/create", ProductCreateView.as_view(), name="product_new"),
    path("products/<slug:slug>", ProductDetailView.as_view(), name="product_detail"),
    path("products/<slug:slug>/edit", ProductUpdateView.as_view(), name="product_edit"),
    path("products/<slug:slug>/delete", ProductDeleteView.as_view(), name="product_delete")
]





