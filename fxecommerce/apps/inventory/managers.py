from django.db import models
from django.db.models import Q


class EmployeeQuerySet(models.QuerySet):
    def search(self, search_query):
        if search_query:
            return self.filter(
                Q(first_name__icontains=search_query) |
                Q(last_name__icontains=search_query)
            )
        return self

class EmployeeManager(models.Manager):
    def get_queryset(self):
        return EmployeeQuerySet(self.model, using=self._db)

    def search(self, search_query):
        return self.get_queryset().search(search_query)

    def get_paginate_by(self, queryset):
        return self.request.GET.get("paginate_by", self.paginate_by)


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

    def get_paginate_by(self, queryset):
        return self.request.GET.get("paginate_by", self.paginate_by)


class CategoryManager(models.Manager):
    def get_paginate_by(self, queryset):
        return self.request.GET.get("paginate_by", self.paginate_by)


class OrderDetailsQuerySet(models.QuerySet):
    def search(self, search_query):
        if search_query:
            return self.filter(
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

    def get_paginate_by(self, queryset):
        return self.request.GET.get("paginate_by", self.paginate_by)





