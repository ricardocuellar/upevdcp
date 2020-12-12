from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import  ListView, TemplateView
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views.generic import CreateView
from django.urls import reverse_lazy

#Forms 
from dashboard.forms import ETPForm
#Models
from users.models import UsersRole
from materias.models import Materia
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
            return render(request, 'coordinadorUPEV/home.html')
        elif rol == "evaluador":
            return render(request, 'evaluadorUPEV/home.html')


#Admin dashboard
@login_required(redirect_field_name=None)
@admin_required
def procesoETPs(request):
    return render(request, 'coordinadorUPEV/procesoETP.html')

@login_required(redirect_field_name=None)
@admin_required
def solicitudesETP(request):
    return render(request, 'coordinadorUPEV/solicitudesETP.html')

@login_required(redirect_field_name=None)
@admin_required
def validarETP(request):
    return render(request, 'coordinadorUPEV/validarETP.html')


@login_required(redirect_field_name=None)
@admin_required
def historialETP(request):
    return render(request, 'coordinadorUPEV/historial.html')

@login_required(redirect_field_name=None)
@admin_required
def crearEquipos(request):
    return render(request, 'coordinadorUPEV/crearEquipos.html')


#ETP (Evaluación técnico pedagogica) (UTEyCV)

# @login_required(redirect_field_name=None)

# def etpCrear(request):
#     """Crear ETP"""
#     return render(request, 'coordinadorUTEyCV/crearETP.html')


class etpCrear(LoginRequiredMixin,CreateView):
    """Return create view"""
    template_name = 'coordinadorUTEyCV/crearETP.html'
    form_class = ETPForm
    success_url = reverse_lazy('dashboard:etpProceso')

    def get_context_data(self, **kwargs):
        """Add user and profile data to context"""
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['usersrole'] = self.request.user.usersrole
        context['materias'] = Materia.objects.all()
        return context

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


# Actividades (Evaluadores)

@login_required(redirect_field_name=None)
@evaluador_required
def tableroActividades(request):
    """Tablero de actividades"""
    return render(request, 'evaluadorUPEV/tableroActividades.html')


@login_required(redirect_field_name=None)
@evaluador_required
def pasadasActividades(request):
    """Actividades pasadas"""
    return render(request, 'evaluadorUPEV/actividadesPasadas.html')




# Test

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