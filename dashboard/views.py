from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from users.models import UsersRole

# Create your views here.

class DashboardView(LoginRequiredMixin, ListView):
    """Return dashboard view"""
    template_name = 'coordinadorUPEV/dashboardUPEV.html'
    model = UsersRole