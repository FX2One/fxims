from django.urls import path
from . import views
from django.contrib.auth import views as auth_view
from .views import EmployeeListView, EmployeeDetailView

app_name = 'users'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('profile/', views.employee_profile, name='employee_profile'),
    path('profile/', views.customer_profile, name='customer_profile'),
    path('profile/update/customer', views.customer_update, name='customer_update'),
    path('profile/update/employee', views.employee_update, name='employee_update'),
    path('login/', auth_view.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_view.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path("employee/", EmployeeListView.as_view(), name="employee"),
    path("employee/<slug:slug>", EmployeeDetailView.as_view(),name="employee_detail"),
]