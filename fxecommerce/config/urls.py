from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from users import views as user_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("inventory.urls", namespace="inventory")),
    path('register/', include('users.urls', namespace='users'))
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

