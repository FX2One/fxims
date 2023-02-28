from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


'''subclassed Forms'''
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import User, Customer, Employee

class CustomerProfileInline(admin.StackedInline):
    model = Customer
    can_delete = False
    verbose_name_plural = 'Customer'
    fk_name = 'user'

class EmployeeProfileInline(admin.StackedInline):
    model = Employee
    can_delete = False
    verbose_name_plural = 'Employee'
    fk_name = 'user'

class CustomUserAdmin(UserAdmin):
    inlines = (CustomerProfileInline, EmployeeProfileInline)
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ('email', 'is_staff', 'is_active', 'is_superuser')
    list_filter = ('email', 'is_staff', 'is_active', 'is_superuser', 'user_type')

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active', 'user_type', 'groups')}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()

        user_type = obj.user_type

        if user_type == 4:
            return [CustomerProfileInline(self.model, self.admin_site)]
        elif user_type == 1:
            return [EmployeeProfileInline(self.model, self.admin_site)]

        return super(CustomUserAdmin, self).get_inline_instances(request, obj)


admin.site.register(User, CustomUserAdmin)
admin.site.register(Employee)
admin.site.register(Customer)



