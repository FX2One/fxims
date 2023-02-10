from django.shortcuts import render
from .forms import CustomUserCreationForm, CustomUserUpdateForm, CustomerUpdateForm, EmployeeUpdateForm
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import GroupRequiredMixin
from django.views.generic import ListView, DetailView, TemplateView
from .models import Employee



def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inventory:home')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'users/register.html', context)


@login_required
def customer_profile(request):
    return render(request, 'users/profile.html')

@login_required
def employee_profile(request):
    return render(request, 'users/profile.html')

class CustomerProfile():
    pass

class EmployeeProfile():
    pass


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

class CustomerProfileUpdate():
    pass

class EmployeeProfileUpdate():
    pass



class EmployeeListView(GroupRequiredMixin, LoginRequiredMixin, ListView):
    model = Employee
    template_name = "inventory/employees.html"
    context_object_name = 'search_results'
    paginate_by = 10
    group_required = ['ExtraStaff', 'Employee']

    def get_queryset(self):
        search_query = self.request.GET.get('q')
        return Employee.objects.search(search_query)


class EmployeeDetailView(GroupRequiredMixin, LoginRequiredMixin, DetailView):
    model = Employee
    template_name = "inventory/employee_detail.html"
    group_required = ['ExtraStaff', 'Employee']
