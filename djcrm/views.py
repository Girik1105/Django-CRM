from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy

from .forms import UserCreateForm

class index(TemplateView):
    template_name = 'index.html'

class thanks(TemplateView):
    template_name = 'thanks.html'

class SignUpView(CreateView):
    template_name = 'registration/registeration.html'
    form_class = UserCreateForm

    def get_success_url(self):
        return reverse_lazy('login')
