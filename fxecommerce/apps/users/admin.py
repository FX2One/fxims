from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

'''subclassed Forms'''
from .models import User, Customer, Employee
from inventory.models import EmployeeTerritory, CustomerCustomerDemo

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

class CustomerCustomerDemoInline(admin.TabularInline):
    model = CustomerCustomerDemo

class CustomerAdmin(admin.ModelAdmin):
    inlines = [CustomerCustomerDemoInline]
    fieldsets = (
        (None, {
            'fields': ('user', 'company_name', 'contact_name', 'contact_title', 'customer_specialist', 'image'),
        }),
        ('Address Info', {
            'fields': ('address', 'city', 'region', 'postal_code', 'country', 'phone', 'fax'),
        }),
    )
    list_display = ('user', 'company_name', 'contact_name', 'contact_title', 'is_verified')
    list_filter = ('is_verified',)
    search_fields = ('company_name', 'contact_name', 'contact_title')

class EmployeeTerritoryInline(admin.TabularInline):
    model = EmployeeTerritory


class EmployeeAdmin(admin.ModelAdmin):
    inlines = [EmployeeTerritoryInline]
    fieldsets = (
        (None, {
            'fields': ('user', 'last_name', 'first_name', 'title', 'title_of_courtesy', 'slug'),
        }),
        ('Personal info', {
            'fields': ('birth_date', 'hire_date', 'address', 'city', 'region', 'postal_code', 'country', 'home_phone', 'extension', 'photo', 'notes'),
        }),
        ('Manager', {
            'fields': ('reports_to',),
        }),
    )

class CustomUserAdmin(UserAdmin):
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




admin.site.register(User, CustomUserAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Customer, CustomerAdmin)



