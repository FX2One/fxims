from django.db import models
from django.db.models import Q
from django.db.models import Prefetch

class ProductQuerySet(models.QuerySet):
    def search(self, search_query):
        if search_query:
            return self.filter(
                Q(product_name__icontains=search_query)
            )
        return self

class ProductManager(models.Manager):
    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)

    def search(self,search_query):
        return self.get_queryset().search(search_query)


class CategoryManager(models.Manager):
    pass


class OrderDetailsQuerySet(models.QuerySet):
    def search(self, search_query):
        if search_query:
            return self.select_related(
                'order_id',
                'order_id__customer_id',
                'order_id__customer_id__user',
                'product_id',
                'product_id__category_id'
            ).filter(
                Q(order_id__order_id__icontains=search_query) |
                Q(product_id__category_id__category_name__icontains=search_query) |
                Q(product_id__product_name__icontains=search_query) |
                Q(quantity__icontains=search_query) |
                Q(order_id__customer_id__user__email__icontains=search_query)
            )
        return self



class OrderDetailsManager(models.Manager):
    def get_queryset(self):
        return OrderDetailsQuerySet(self.model, using=self._db)

    def search(self, search_query):
        return self.get_queryset().search(search_query)







