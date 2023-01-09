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

class ProductManager(models.Manager):
    def get_paginate_by(self, queryset):
        return self.request.GET.get("paginate_by", self.paginate_by)


class CategoryManager(models.Manager):
    pass


class OrderManager(models.Manager):
    pass





