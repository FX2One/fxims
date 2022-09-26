from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inv/', include("fxecommerce.inventory.urls", namespace="inventory")),
]
