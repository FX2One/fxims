from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path("inventory/", include("fxecommerce.inventory.urls", namespace="inventory")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

