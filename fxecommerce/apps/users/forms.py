from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User, Customer, Employee
from django import forms


class EmployeeUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email',)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email.endswith('@e.com'):
            raise forms.ValidationError("Only Employees allowed to register here.")
        return email

class CustomerUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email',)



'''subclass UserCreationForm to match new CustomUser'''
'''class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email',)'''


'''subclass UserCreationForm to match new CustomUser'''
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('email',)


class CustomUserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class CustomerUpdateForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = [
            'image',
            'company_name',
            'contact_name',
            'contact_title',
            'address',
            'city',
            'region',
            'postal_code',
            'country',
            'phone',
            'fax'
        ]

class EmployeeUpdateForm(forms.ModelForm):
    birth_date = forms.DateField(input_formats=['%Y-%m-%d'], help_text='Enter date in the format YYYY-MM-DD')
    hire_date = forms.DateField(input_formats=['%Y-%m-%d'], help_text='Enter date in the format YYYY-MM-DD')
    class Meta:
        model = Employee
        fields = [
            'last_name',
            'first_name',
            'title',
            'title_of_courtesy',
            'birth_date',
            'hire_date',
            'address',
            'city',
            'region',
            'postal_code',
            'country',
            'home_phone',
            'extension',
            'photo',
            'notes',
            'reports_to',
            'photo_path',
            'territories'
        ]
