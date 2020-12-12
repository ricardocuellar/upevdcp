from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import  ListView, TemplateView
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

#Models
from users.models import UsersRole
from dashboard.decorators import admin_required, uteycv_required, evaluador_required


# Create your views here.

# class DashboardView(LoginRequiredMixin,TemplateView):
#     template_name = "coordinadorUPEV/dashboardUPEV.html"


@login_required
def DashboardTemplate(request):
        user_id = request.user.pk
        rol = UsersRole.objects.get(user_id=user_id).role 
        if rol == "uteycv":
            return render(request, 'coordinadorUTEyCV/home.html')
        elif rol == "admin":
            return render(request, 'coordinadorUPEV/dashboardUPEV.html')
        elif rol == "evaluador":
            return render(request, 'evaluadorUPEV/dashboardEvaluador.html')



#ETP (Evaluación técnico pedagogica) (UTEyCV)

@login_required(redirect_field_name=None)
@uteycv_required
def etpCrear(request):
    """Crear ETP"""
    return render(request, 'coordinadorUTEyCV/crearETP.html')



@login_required(redirect_field_name=None)
@uteycv_required
def etpProceso(request):
    """Ver procesos de ETPs"""
    return render(request, 'coordinadorUTEyCV/procesoETP.html')


@login_required(redirect_field_name=None)
@uteycv_required
def etpSolicitudes(request):
    """Ver procesos de ETPs"""
    return render(request, 'coordinadorUTEyCV/solicitudesETP.html')




@login_required(redirect_field_name=None)
@admin_required
def test_admin(request):
    return render(request, 'coordinadorUPEV/testUPEV.html')


@login_required(redirect_field_name=None)
@uteycv_required
def test_uteycv(request):
    return render(request, 'coordinadorUTEyCV/testUTEyCV.html')


@login_required(redirect_field_name=None)
@evaluador_required
def test_evaluador(request):
    return render(request, 'evaluadorUPEV/testEvaluador.html')