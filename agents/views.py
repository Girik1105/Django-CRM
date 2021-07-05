from django.shortcuts import render
from django.urls import reverse_lazy, reverse

from django.core.mail import send_mail

from django.views.generic import TemplateView, ListView, CreateView, DeleteView, UpdateView, DetailView, View
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from leads.models import Agent
from . import forms
from djcrm.forms import UserCreateForm

from django.contrib.auth import get_user_model
User = get_user_model()

import random
# Create your views here.
class AgentListView(LoginRequiredMixin, UserPassesTestMixin,  ListView):

    login_url = '/login/'

    template_name = 'agents/agent_list.html'

    def get_queryset(self):
        return Agent.objects.filter(organisation=self.request.user.userprofile)

    def test_func(self):
        if self.request.user.is_organiser:
            return True


class AgentCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    login_url = '/login/'
    template_name = 'agents/agent_create.html'

    model = Agent
    form_class = forms.AgentModelForm

    def get_success_url(self):
        return reverse('agents:agent-list')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_agent = True
        user.is_organiser = False
        temp_pass = f"{random.randint(15000000, 95000000)}"
        user.set_password(temp_pass)
        user.save()

        Agent.objects.create(user=user, organisation=self.request.user.userprofile)

        send_mail(
            subject="You are invited to be an agent",
            message=f"You have been entered in the system as an agent on CRM, Please login to continue working \n Your credentials: \n First Name:{user.first_name} \n Last Name:{user.last_name} \n username:{user.username} \n Your temporary password: {temp_pass}",
            from_email='test@test.com',
            recipient_list=[user.email]
        )

        return super(AgentCreateView, self).form_valid(form)

    def test_func(self):
        if self.request.user.is_organiser:
            return True


class AgentDetailView(LoginRequiredMixin, UserPassesTestMixin,  DetailView):
    login_url = '/login/'
    template_name = 'agents/agent_detail.html'

    model = Agent

    def get_queryset(self):
        return Agent.objects.filter(organisation=self.request.user.userprofile)

    def test_func(self):
        if self.request.user.is_organiser:
            return True




class AgentUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    template_name = 'agents/agent_update.html'

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

    def get_success_url(self):
        return reverse('agents:agent-list')

    def get_queryset(self):
        return User.objects.filter(username=self.request.user.username)

    def form_valid(self, form):
        user = form.save(commit=False)
        user.save()

        return super(AgentUpdateView, self).form_valid(form)



class AgentDeleteView(LoginRequiredMixin, UserPassesTestMixin,  DeleteView):
    login_url = '/login/'
    template_name = 'agents/agent_delete.html'

    model = Agent

    def get_success_url(self):
        return reverse('agents:agent-list')

    def get_queryset(self):
        return Agent.objects.filter(organisation=self.request.user.userprofile)

    def test_func(self):
        if self.request.user.is_organiser:
            return True
