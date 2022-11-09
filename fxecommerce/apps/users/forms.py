from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User

'''subclass UserCreationForm to match new CustomUser'''


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email',)


'''subclass UserCreationForm to match new CustomUser'''


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('email',)
