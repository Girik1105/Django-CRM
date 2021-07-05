from django import forms
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import get_user_model
User = get_user_model()

class UserCreateForm(UserCreationForm):
    email = forms.EmailField()

    class Meta():
        model = User
        fields = (
            'first_name',
            'last_name',
            'username',
            'email',
            'phone_number',
            'organisation_name',
            'address',
            'profile_picture',
        )
