from django.db import models


class EmployeeManager(models.Manager):
    pass


class ProductManager(models.Manager):
    def get_paginate_by(self, queryset):
        return self.request.GET.get("paginate_by", self.paginate_by)


class CategoryManager(models.Manager):
    pass


class OrderManager(models.Manager):
    pass




