from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm

from Authentication.models import User


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'profile_pic')


class UserUpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'profile_pic')
