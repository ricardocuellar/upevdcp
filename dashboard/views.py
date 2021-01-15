from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.decorators.csrf import requires_csrf_token
from django.views.generic import  ListView, TemplateView
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views.generic import CreateView
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse
from django.utils import timezone
#from extra_views import CreateWithInlinesView, InlineFormSet
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User 
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
#Forms 
from dashboard.forms import ETPForm, EquipoForm
from comentarios.forms import ComentarioForm
from comentarios.models import Comentario

#Models
from users.models import UsersRole
from materias.models import Materia
from etps.models import ETP
from carreras.models import Carrera
from unidadAcademica.models import UnidadAcademica
from equipos.models import Equipo
from dashboard.decorators import admin_required, uteycv_required, evaluador_required
from tareas.models import Tarea








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
        context['etps'] = ETP.objects.filter(solicitud_aprobada=1)
        
        return context

    def form_valid(self,form):
        cleaned_data = form.cleaned_data
        evaluadores_data = [cleaned_data['evaluador_originalidad'].pk,cleaned_data['evaluador_estilos'].pk,cleaned_data['evaluador_pedagogo'].pk,cleaned_data['evaluador_comunicologo'].pk]
        id_etp = cleaned_data['id_etp'].pk
        idx = 0
        while(idx < 4):
            user_evaluador = UsersRole.objects.get(user_id=evaluadores_data[idx])
            user_evaluador.disponible = 1
            user_evaluador.save()

            user_tareas = Tarea()
            user_tareas.estado_tarea = 'Pendientes'
            user_tareas.user_tasks_id = evaluadores_data[idx]
            user_tareas.etp_task_id = id_etp
            user_tareas.save()
            idx+=1

        self.object = form.save()

        return HttpResponseRedirect(self.get_success_url())
   



#ETP (Evaluación técnico pedagogica) (UTEyCV)

# @login_required(redirect_field_name=None)
# def etpCrear(request):
#      """Crear ETP"""
#      context = {}
#      if request.method == 'POST':
#          uploaded_file = request.FILES['documento']
#          print(uploaded_file.name)
#          fs = FileSystemStorage()
#          name = fs.save(uploaded_file.name, uploaded_file)
#          url = fs.url(name)
#          context['url'] = fs.url(name)
#      return render(request, 'coordinadorUTEyCV/crearETP.html', context)
    

def etpCrear(request):
    if request.method == 'POST':
        form = ETPForm(request.POST, request.FILES)
        if form.is_valid():
            user = User.objects.get(id= request.POST['solicitante'])
            print(request.POST['solicitante'])
            form.instance.solicitante = user
            form.save()
            messages.success(request, 'ETP Creada correctamente')
            return render(request, 'coordinadorUTEyCV/crearETP.html')
        
    else:
        form = ETPForm()
    return render(request, 'coordinadorUTEyCV/crearETP.html',{
        'form': form
    })

# class etpCrear(LoginRequiredMixin,CreateView):
#     """Return create view"""
#     template_name = 'coordinadorUTEyCV/crearETP.html'
#     model=ETP
#     form_class = ETPForm
#     success_url = reverse_lazy('dashboard:etpSolicitudes')

    

#     def get_context_data(self, **kwargs):
#         """Add user and profile data to context"""
#         context = super().get_context_data(**kwargs)
#         context['user'] = self.request.user
#         context['materias'] = Materia.objects.all()
#         return context

#     def upload(self,request):
#         if request.method == 'POST':
#             uploaded_file = request.FILES['documento']
#             print('nombre:' + uploaded_file.name)

#     def form_valid(self,form):
#         cleaned_data = form.cleaned_data
#         print(cleaned_data)
#         file = [cleaned_data['documento']]
#         print(file)
#         self.object = form.save()
#         return HttpResponseRedirect(self.get_success_url())


@login_required(redirect_field_name=None)
@uteycv_required
def etpProceso(request):
    """Ver procesos de ETPs"""
    user = request.user.pk
    etps = ETP.objects.filter(solicitante_id = user)
    context = {'etps':etps}
    return render(request, 'coordinadorUTEyCV/procesoETP.html', context)


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
    tareas = Tarea.objects.filter(user_tasks_id=user_id)
    print(tareas)
    equipo = Equipo.objects
    
    #todo meter aqui los solicitantes_id
    if role == 'originalidad':
        equipo_member_id = equipo.filter(evaluador_originalidad_id=user_id)
    elif role == 'pedagogo':
        equipo_member_id = equipo.filter(evaluador_pedagogo_id=user_id)
    elif role == 'comunicologo':
        equipo_member_id = equipo.filter(evaluador_comunicologo_id=user_id)
    elif role == 'estilos':
        equipo_member_id = equipo.filter(evaluador_estilos_id=user_id)


    if request.method == 'POST':
        if request.POST['solicitud'] == 'validar':
            tareas = Tarea.objects.filter(user_tasks_id=request.POST['user']).get(etp_task_id=request.POST['etp'])
            print(tareas)
            user_id = UsersRole.objects.get(user_id=request.POST['user'])
            etp = ETP.objects.get(pk=request.POST['etp'])     
            tareas.estado_tarea = 'Haciendo'
            if user_id.evaluador == 'originalidad':
                etp.estado = 'Originalidad'
            elif user_id.evaluador == 'pedagogo':
                etp.estado = 'Pedagógico'
            elif user_id.evaluador == 'comunicologo':
                etp.estado = 'Comunicación'
            elif user_id.evaluador == 'estilos':
                etp.estado = 'Estilos'
            tareas.save()    
            etp.save()

        elif request.POST['solicitud'] == 'revisar':
            tareas = Tarea.objects.filter(user_tasks_id=request.POST['evaluador']).get(etp_task_id=request.POST['etp'])
            etp = ETP.objects.get(pk=request.POST['etp']) 
            tareas.estado_tarea = 'Espera'
            etp.estado = 'Espera'
            etp.pendientes = 1
            tareas.save()
            etp.save()
            form=ComentarioForm(request.POST)
            if form.is_valid():
                user = User.objects.get(id= request.POST['evaluador'])          
                form.instance.evaluador = user
                form.instance.etp = etp
                comentario = form.save()
                return redirect('/dashboard/tablero-actividades')

        elif request.POST['solicitud'] == 'terminar':
            tareas = Tarea.objects.filter(user_tasks_id=request.POST['user']).get(etp_task_id=request.POST['etp'])
            tareas.estado_tarea = 'Hecho'
            tareas.save()

            etp = ETP.objects.get(pk=request.POST['etp']) 
            if role == 'originalidad':
                etp.estado = 'Pedagógico'
            elif role == 'pedagogo':
                etp.estado = 'Comunicación'
            elif role == 'comunicologo':
                etp.estado = 'Estilos'
            elif role == 'estilos':
                etp.estado = 'Terminado'
            etp.save()

            return redirect('/dashboard/tablero-actividades')

    # equipo = []
    # for etp in etps:
    #     equipo.append(etp.estado)
    form = ComentarioForm()
    context = {'etps':etps,'rol': role, 'equipo_member':equipo_member_id,'equipo':equipo,'tareas':tareas,'user_id':user_id, 'form':form}
    return render(request, 'evaluadorUPEV/tableroActividades.html', context)




def home(request):
    if request.method == "POST":
        form=ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save()
            return render(request, 'comentario/index.html',{'form':form})
    
    form = ComentarioForm()
    return render(request, 'comentario/index.html',{'form':form})


def verComentario(request, comentarioID):
    comentario = Comentario.objects.get(id=comentarioID)
    return render(request,'comentario/comentarioDetail.html',{'comentario':comentario})












@login_required(redirect_field_name=None)
@evaluador_required
def pasadasActividades(request):
    """Actividades pasadas"""
    return render(request, 'evaluadorUPEV/actividadesPasadas.html')


@login_required(redirect_field_name=None)
@evaluador_required
def cambiarEstadoETP(request):
    """Cambiar estado"""
    
    
    
    return redirect('evaluadorUPEV/tableroActividades.html')




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