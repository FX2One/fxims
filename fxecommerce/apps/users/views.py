from django.shortcuts import render
from .forms import EmployeeUserCreationForm, CustomerUserCreationForm, CustomUserUpdateForm, CustomerUpdateForm, \
    EmployeeUpdateForm
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import GroupRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, View
from .models import Employee, Customer
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from .forms import EmployeeUserCreationForm, CustomerUserCreationForm

from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth import get_user_model

from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView, PasswordChangeView


class RegisterView(CreateView):
    def send_confirmation_email(self, user):
        current_site = get_current_site(self.request)
        subject = 'FXIMS Account Activation'
        message = render_to_string('users/account_activation.html', {
            'user': user,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': account_activation_token.make_token(user),
        })
        user.email_user(subject, message)

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False  # Deactivate account till it is confirmed
        user.save()

        self.send_confirmation_email(user)

        messages.success(self.request, ('Please Confirm your email to complete registration.'))

        return redirect('users:login')


class EmployeeRegisterView(RegisterView):
    template_name = 'users/register_employee.html'
    form_class = EmployeeUserCreationForm
    success_url = reverse_lazy('inventory:home')

    def form_valid(self, form):
        form.instance.user_type = 1
        return super().form_valid(form)


class CustomerRegisterView(RegisterView):
    template_name = 'users/register_customer.html'
    form_class = CustomerUserCreationForm
    success_url = reverse_lazy('inventory:home')

    def form_valid(self, form):
        form.instance.user_type = 4
        return super().form_valid(form)


class AccountActivationView(View):
    def get(self, request, uidb64, token, *args, **kwargs):
        user = None

        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            User = get_user_model()
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            pass

        if user is not None and account_activation_token.check_token(user, token):
            user.is_active = True
            user.save()
            login(request, user)
            message = ('Your account has been confirmed.')
        else:
            message = ('The confirmation link was invalid, possibly because it has already been used.')

        messages.success(request, message) if user else messages.warning(request, message)
        return redirect('inventory:home')


class CustomPasswordResetView(PasswordResetView):
    success_url = reverse_lazy("users:password_reset_done")


class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    success_url = reverse_lazy("users:password_reset_complete")


class CustomPasswordChangeView(PasswordChangeView):
    success_url = reverse_lazy("users:password_change_done")


@login_required
def customer_profile(request):
    return render(request, 'users/profile.html')


@login_required
def employee_profile(request):
    return render(request, 'users/profile.html')


@login_required
def customer_update(request):
    if request.method == 'POST':
        user_form = CustomUserUpdateForm(request.POST, instance=request.user)
        customer_form = CustomerUpdateForm(request.POST, request.FILES, instance=request.user.customer)
        if user_form.is_valid() and customer_form.is_valid():
            user_form.save()
            customer_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect('users:customer_profile')
    else:
        user_form = CustomUserUpdateForm(instance=request.user)
        customer_form = CustomerUpdateForm(instance=request.user.customer)
    context = {
        'user_form': user_form,
        'customer_form': customer_form
    }
    return render(request, 'users/customer_update.html', context)


@login_required
def employee_update(request):
    if request.method == 'POST':
        user_form = CustomUserUpdateForm(request.POST, instance=request.user)
        employee_form = EmployeeUpdateForm(request.POST, request.FILES, instance=request.user.employee)
        if user_form.is_valid() and employee_form.is_valid():
            user_form.save()
            employee_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect('users:employee_profile')
    else:
        user_form = CustomUserUpdateForm(instance=request.user)
        employee_form = EmployeeUpdateForm(instance=request.user.employee)
    context = {
        'user_form': user_form,
        'employee_form': employee_form
    }
    return render(request, 'users/employee_update.html', context)


class EmployeeListView(GroupRequiredMixin, LoginRequiredMixin, ListView):
    model = Employee
    template_name = "users/employees.html"
    context_object_name = 'search_results'
    paginate_by = 10
    group_required = ['ExtraStaff', 'Employee']

    def get_queryset(self):
        search_query = self.request.GET.get('q')
        return Employee.objects.search(search_query)

    def get_paginate_by(self, queryset):
        return self.request.GET.get("paginate_by", self.paginate_by)


class EmployeeDetailView(GroupRequiredMixin, LoginRequiredMixin, DetailView):
    model = Employee
    template_name = "users/employee_detail.html"
    group_required = ['ExtraStaff', 'Employee']


class CustomerListView(GroupRequiredMixin, LoginRequiredMixin, ListView):
    model = Customer
    template_name = "users/customers.html"
    context_object_name = 'search_results'
    paginate_by = 10
    group_required = ['Employee', 'ExtraStaff']

    def get_queryset(self):
        search_query = self.request.GET.get('q')
        return Customer.objects.search(search_query)

    def get_paginate_by(self, queryset):
        return self.request.GET.get("paginate_by", self.paginate_by)


class CustomerDetailView(GroupRequiredMixin, LoginRequiredMixin, DetailView):
    model = Customer
    template_name = "users/customer_detail.html"
    group_required = ['ExtraStaff', 'Employee']
