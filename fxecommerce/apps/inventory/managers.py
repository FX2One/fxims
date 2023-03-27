from django.db import models
from django.db.models import Q


class ProductQuerySet(models.QuerySet):
    def search(self, search_query):
        if search_query:
            return self.select_related('category_id').filter(
                Q(product_name__icontains=search_query) |
                Q(category_id__category_name__icontains=search_query)
            )
        return self.select_related('category_id')


class ProductManager(models.Manager):
    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)

    def search(self,search_query):
        return self.get_queryset().search(search_query)


class CategoryQuerySet(models.QuerySet):
    def search(self, search_query):
        if search_query:
            return self.filter(
                Q(category_name__icontains=search_query)
            )
        return self


class CategoryManager(models.Manager):
    def get_queryset(self):
        return CategoryQuerySet(self.model, using=self._db)

    def search(self,search_query):
        return self.get_queryset().search(search_query)


class OrderDetailsQuerySet(models.QuerySet):
    def search(self, search_query):
        if search_query:
            return self.select_related(
                'order_id',
                'product_id',
                'product_id__category_id',
                'created_by').filter(
                Q(order_id__order_id__icontains=search_query) |
                Q(product_id__category_id__category_name__icontains=search_query) |
                Q(product_id__product_name__icontains=search_query) |
                Q(quantity__icontains=search_query) |
                Q(created_by__email__icontains=search_query)
            )
        return self.select_related('order_id', 'product_id', 'product_id__category_id', 'created_by')


class OrderDetailsManager(models.Manager):
    def get_queryset(self):
        return OrderDetailsQuerySet(self.model, using=self._db)

    def search(self, search_query):
        return self.get_queryset().search(search_query)


class OrderQuerySet(models.QuerySet):
    def search(self, search_query):
        if search_query:
            return self.filter(
                Q(order_id__icontains=search_query)
            )
        return self


class OrderManager(models.Manager):
    def get_queryset(self):
        return OrderQuerySet(self.model, using=self._db)

    def search(self, search_query):
        return self.get_queryset().search(search_query)