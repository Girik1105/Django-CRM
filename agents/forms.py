from django import forms

from django.contrib.auth import get_user_model
User = get_user_model()


# from leads.models import Agent

class AgentModelForm(forms.ModelForm):
    class Meta():
        model = User
        fields = (
            'first_name',
            'last_name',
            'username',
            'email',
            'phone_number',
            'address',
            'profile_picture',
        )
