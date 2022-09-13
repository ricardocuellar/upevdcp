#Django
from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import views as auth_views

# Create your views here.

#Login system
class LoginView(auth_views.LoginView):
    """Login View"""
    template_name = 'users/login.html'


class LogoutView(LoginRequiredMixin, auth_views.LogoutView):
    """Logout view"""
    template_name = 'users/logged_auth.html'
