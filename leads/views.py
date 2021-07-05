from django.shortcuts import render
from django.urls import reverse_lazy, reverse

from django.views.generic import (TemplateView,
                                  ListView,
                                  CreateView,
                                  DeleteView,
                                  UpdateView,
                                  DetailView,
                                  FormView,
                                  View)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from . import models, forms

from django.core.mail import send_mail

# Create your views here.
class LeadsListView(LoginRequiredMixin, ListView):

    login_url = '/login/'
    template_name = 'leads/lead_list.html'
    context_object_name = "leads"

    def get_queryset(self):

        if self.request.user.is_organiser:
            queryset = models.lead.objects.filter(organisation=self.request.user.userprofile, agent__isnull=False)

        else:
            queryset = models.lead.objects.filter(organisation=self.request.user.agent.organisation, agent__isnull=False)
            queryset = queryset.filter(agent__user=self.request.user)

        return queryset

    def get_context_data(self, **kwargs):
        context = super(LeadsListView, self).get_context_data(**kwargs)
        if self.request.user.is_organiser:
            queryset = models.lead.objects.filter(organisation=self.request.user.userprofile, agent__isnull=True)
            context.update({
                "unassingned_leads": queryset
            })
        return context

class CreateLeadView(LoginRequiredMixin, UserPassesTestMixin, CreateView):

    login_url = '/login/'

    template_name = 'leads/lead_create.html'
    model = models.lead
    form_class = forms.LeadForm

    def get_success_url(self):
        return reverse_lazy('leads:lead-list')

    def form_valid(self, form):
        lead = form.save(commit=False)
        lead.organisation =  self.request.user.userprofile
        lead.save()
        #To send emails
        send_mail(
            subject="A lead has been created",
            message="Visit the site to view the new lead",
            from_email='test@test.com',
            recipient_list=['test2@test.com']
        )
        return super(CreateLeadView, self).form_valid(form)


    def get_form_kwargs(self, **kwargs):
        kwargs = super(CreateLeadView, self).get_form_kwargs(**kwargs)
        kwargs.update({
            "request":self.request,
        })
        return kwargs

    def test_func(self):
        if self.request.user.is_organiser:
            return True


class DetailLeadView(LoginRequiredMixin, DetailView):

    login_url = '/login/'

    template_name = 'leads/lead_detail.html'
    model = models.lead


class UpdateLeadView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):

    login_url = '/login/'

    template_name = 'leads/lead_update.html'
    model = models.lead
    form_class = forms.LeadForm

    def get_success_url(self):
        return reverse('leads:lead-detail', kwargs={'pk':self.object.pk})

    def get_queryset(self):
        return models.lead.objects.filter(organisation=self.request.user.userprofile)

    def get_form_kwargs(self, **kwargs):
        kwargs = super(UpdateLeadView, self).get_form_kwargs(**kwargs)
        kwargs.update({
            "request":self.request,
        })
        return kwargs

    def test_func(self):
        if self.request.user.is_organiser:
            return True


class DeleteLeadView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):

    login_url = '/login/'

    template_name = 'leads/lead_delete.html'
    model = models.lead

    def get_success_url(self):
        return reverse('leads:lead-list')

    def get_queryset(self):
        return models.lead.objects.filter(organisation=self.request.user.userprofile)

    def test_func(self):
        if self.request.user.is_organiser:
            return True


class CategoryListView(LoginRequiredMixin, ListView):

    login_url = '/login/'

    template_name = 'category/cat_list.html'
    context_object_name = "cat_list"

    def get_context_data(self, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        user = self.request.user

        if user.is_organiser:
            queryset = models.lead.objects.filter(
                organisation=user.userprofile
            )
        else:
            queryset = models.lead.objects.filter(
                organisation=user.agent.organisation
            )

        context.update({
            "unassigned_lead_count": queryset.filter(agent__isnull=True).count()
        })
        return context

    def get_queryset(self):

        if self.request.user.is_organiser:
            queryset = models.Category.objects.filter(organisation=self.request.user.userprofile)

        else:
            queryset = models.Category.objects.filter(organisation=self.request.user.agent.organisation)

        return queryset


class CategoryDetailView(LoginRequiredMixin, DetailView):
    template_name = "category/cat_detail.html"
    context_object_name = 'category'

    def get_context_data(self, **kwargs):
        context = super(CategoryDetailView, self).get_context_data(**kwargs)
        user = self.request.user

        queryset = models.lead.objects.filter(category=self.get_object())
        leads = self.get_object().leads.all()

        context.update({
            "leads": leads
        })
        return context

    def get_queryset(self):

        if self.request.user.is_organiser:
            queryset = models.Category.objects.filter(organisation=self.request.user.userprofile)

        else:
            queryset = models.Category.objects.filter(organisation=self.request.user.agent.organisation)

        return queryset

class CategoryCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    template_name = 'category/cat_create.html'
    model = models.Category

    form_class = forms.CategoryForm

    def form_valid(self, form):
        cat = form.save(commit=False)
        cat.organisation = self.request.user.userprofile
        form.save()

        return super(CategoryCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('leads:category-list')

    def test_func(self):
        if self.request.user.is_organiser:
            return True

class CategoryUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = 'category/cat_update.html'
    model = models.Category

    form_class = forms.CategoryForm

    def get_success_url(self):
        return reverse('leads:category-list')

    def test_func(self):
        if self.request.user.is_organiser:
            return True

class CategoryDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):

    template_name = 'category/cat_delete.html'
    model = models.Category

    def get_success_url(self):
        return reverse('leads:category-list')

    def test_func(self):
        if self.request.user.is_organiser:
            return True
