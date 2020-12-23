from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import  ListView, TemplateView
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views.generic import CreateView
#from extra_views import CreateWithInlinesView, InlineFormSet
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User 

#Forms 
from dashboard.forms import ETPForm, EquipoForm
#Models
from users.models import UsersRole
from materias.models import Materia
from etps.models import ETP
from carreras.models import Carrera
from unidadAcademica.models import UnidadAcademica
from equipos.models import Equipo
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
    etps = ETP.objects.filter(solicitud_aprobada=1)
    contex = {'etps': etps}
    return render(request, 'coordinadorUPEV/procesoETP.html',contex)

@login_required(redirect_field_name=None)
@admin_required
def solicitudesETP(request, escuela=None):
    if request.method == 'POST':
        if request.POST['solicitud'] == 'validar':
            etp = ETP.objects.get(pk=request.POST['user'])
            etp.solicitud_aprobada = 1
            etp.save()
    
    etps = ETP.objects.filter(solicitud_aprobada=0)
    materias = Materia.objects.all()
    
    
    contex = {'etps': etps, 'materia':materias,}
    return render(request, 'coordinadorUPEV/solicitudesETP.html',contex)

@login_required(redirect_field_name=None)
@admin_required
def validarETP(request):
    etps = ETP.objects.filter(solicitud_aprobada=1)
    contex = {'etps': etps}
    return render(request, 'coordinadorUPEV/validarETP.html',contex)


@login_required(redirect_field_name=None)
@admin_required
def historialETP(request):
    return render(request, 'coordinadorUPEV/historial.html')


@login_required(redirect_field_name=None)
@admin_required
def verEquipos(request):
    equipos = Equipo.objects.all()
    context = {'equipos':equipos}
    return render(request, 'coordinadorUPEV/verEquipos.html',context)



#@login_required(redirect_field_name=None)
#@admin_required
class crearEquipos(LoginRequiredMixin,CreateView):
    template_name = 'coordinadorUPEV/crearEquipos.html'
    model= Equipo
    form_class = EquipoForm
    success_url = reverse_lazy('dashboard:verEquipos')

    def get_context_data(self, **kwargs):
        """Add user and profile data to context"""
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['evaluadores'] = UsersRole.objects.filter(role="evaluador").filter(disponible=1)
        context['etps'] = ETP.objects.filter(solicitud_aprobada=0)
        
        return context

    def form_valid(self,form):
        cleaned_data = form.cleaned_data
        evaluadores_data = [cleaned_data['evaluador_originalidad'].pk,cleaned_data['evaluador_estilos'].pk,cleaned_data['evaluador_pedagogo'].pk,cleaned_data['evaluador_comunicologo'].pk]
        idx = 0
        while(idx < 4):
            user_evaluador = UsersRole.objects.get(user_id=evaluadores_data[idx])
            user_evaluador.disponible = 0
            user_evaluador.save()
            idx+=1

        self.object = form.save()

        return HttpResponseRedirect(self.get_success_url())
   



#ETP (Evaluación técnico pedagogica) (UTEyCV)

# @login_required(redirect_field_name=None)

# def etpCrear(request):
#     """Crear ETP"""
#     return render(request, 'coordinadorUTEyCV/crearETP.html')


class etpCrear(LoginRequiredMixin,CreateView):
    """Return create view"""
    template_name = 'coordinadorUTEyCV/crearETP.html'
    model=ETP
    form_class = ETPForm
    success_url = reverse_lazy('dashboard:etpSolicitudes')

    def get_context_data(self, **kwargs):
        """Add user and profile data to context"""
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['materias'] = Materia.objects.all()
        return context

    def form_valid(self,form):
        self.object = form.save()
        return HttpResponseRedirect(self.get_success_url())


@login_required(redirect_field_name=None)
@uteycv_required
def etpProceso(request):
    """Ver procesos de ETPs"""
    
    return render(request, 'coordinadorUTEyCV/procesoETP.html')


@login_required(redirect_field_name=None)
@uteycv_required
def etpSolicitudes(request):
    """Ver procesos de ETPs"""
    user = request.user.pk
    etps = ETP.objects.filter(solicitante_id = user)
    context = {'etps':etps}
    return render(request, 'coordinadorUTEyCV/solicitudesETP.html',context)


# Actividades (Evaluadores)

@login_required(redirect_field_name=None)
@evaluador_required
def tableroActividades(request):
    """Tablero de actividades"""
    etps = ETP.objects.filter(revision=0).filter(solicitud_aprobada=1)
    user_id = request.user.pk
    role = request.user.usersrole.evaluador
    equipo = Equipo.objects
    if role == 'originalidad':
        equipo_member_id = equipo.filter(evaluador_originalidad_id=user_id)
    elif role == 'pedagogo':
        equipo_member_id = equipo.filter(evaluador_pedagogo_id=user_id)
    elif role == 'comunicologo':
        equipo_member_id = equipo.filter(evaluador_comunicologo_id=user_id)
    elif role == 'estilos':
        equipo_member_id = equipo.filter(evaluador_estilos_id=user_id)

    # equipo = []
    # for etp in etps:
    #     equipo.append(etp.estado)
    context = {'etps':etps,'rol': role, 'equipo_member':equipo_member_id,'equipo':equipo}
    return render(request, 'evaluadorUPEV/tableroActividades.html', context)


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