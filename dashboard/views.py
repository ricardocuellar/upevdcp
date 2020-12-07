from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import  ListView, TemplateView
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
#Models
from users.models import UsersRole

# Create your views here.

# class DashboardView(LoginRequiredMixin,TemplateView):
#     template_name = "coordinadorUPEV/dashboardUPEV.html"


@login_required
def DashboardTemplate(request):
        user_id = request.user.pk
        rol = UsersRole.objects.get(user_id=user_id).role 
        if rol == "uteycv":
            return render(request, 'coordinadorUTEyCV/dashboardUTEyCV.html')
        elif rol == "admin":
            return render(request, 'coordinadorUPEV/dashboardUPEV.html')
        elif rol == "evaluador":
            return render(request, 'evaluadorUPEV/dashboardEvaluador.html')
        
            