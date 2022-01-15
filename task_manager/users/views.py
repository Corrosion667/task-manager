from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from task_manager.users.forms import SignupForm
from task_manager.users.models import User


class MainPageView(TemplateView):
    """View for main (home) site page."""

    template_name = 'main_page.html'


class SignupView(CreateView):
    """View for signup page."""

    model = User
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
    form_class = SignupForm


class LoginView(TemplateView):
    """View for users page."""

    template_name = 'login.html'


class UserLogoutView(LogoutView):

    next_page = reverse_lazy('main')


class UsersListView(TemplateView):
    """View for users page."""

    template_name = 'users.html'
