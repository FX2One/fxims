from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User, Customer
from django import forms

'''subclass UserCreationForm to match new CustomUser'''
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email','user_type')


'''subclass UserCreationForm to match new CustomUser'''
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('email',)


class CustomUserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class ProfileUpdateForm(forms.ModelForm):
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