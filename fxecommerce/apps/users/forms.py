from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

'''subclass UserCreationForm to match new CustomUser'''
class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('email',)


'''subclass UserCreationForm to match new CustomUser'''
class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email',)

