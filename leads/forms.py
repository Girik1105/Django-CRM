from django import forms

from . import models

class LeadForm(forms.ModelForm):

    class Meta():
        model = models.lead
        fields = (
            'first_name',
            'last_name',
            'email',
            'phone_number',
            'address',
            'source',
            'description',
            'agent',
            'category',
            'profile_picture',
        )

    def __init__(self, *args, **kwargs):
        request = kwargs.pop('request')
        agents = models.Agent.objects.filter(organisation=request.user.userprofile)
        category = models.Category.objects.filter(organisation=request.user.userprofile)
        super(LeadForm, self).__init__(*args, **kwargs)
        self.fields["agent"].queryset = agents
        self.fields["category"].queryset = category

class CategoryForm(forms.ModelForm):

    class Meta():
        model = models.Category
        fields = (
            'name',
        )
