from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import EmployeeListView, EmployeeDetailView, EmployeeRegisterView, CustomerRegisterView, CustomerListView, CustomerDetailView, AccountActivationView, CustomPasswordResetView, CustomPasswordResetConfirmView, CustomPasswordChangeView


app_name = 'users'

urlpatterns = [
    path('register/employee/', EmployeeRegisterView.as_view(), name='register_employee'),
    path('register/customer/', CustomerRegisterView.as_view(), name='register_customer'),
    path('activate/<uidb64>/<token>/', AccountActivationView.as_view(), name='activate'),
    path('profile/', views.employee_profile, name='employee_profile'),
    path('profile/', views.customer_profile, name='customer_profile'),
    path('profile/update/customer', views.customer_update, name='customer_update'),
    path('profile/update/employee', views.employee_update, name='employee_update'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('password-reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('password-change/', CustomPasswordChangeView.as_view(), name='password_change'),
    path('password-change/done', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('employee/', EmployeeListView.as_view(), name='employee'),
    path('employee/<slug:slug>', EmployeeDetailView.as_view(),name='employee_detail'),
    path('customer', CustomerListView.as_view(), name='customer'),
    path('customer/<slug:slug>', CustomerDetailView.as_view(), name='customer_detail'),
]