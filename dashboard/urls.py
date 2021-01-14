"""Dashboard URLs"""

#Django
from django.urls import path
from django.views.generic import TemplateView


# Views 
from dashboard import views

urlpatterns = [
    
    #Management
    path(
        route='', 
        view= views.DashboardTemplate,
        #view= views.DashboardView.as_view(),
        name='dashboard'
        ),
    #Administrador dashboard
    path(
        route='etps-en-proceso',
        view= views.procesoETPs,
        name= 'procesoETPs'
    ),
    path(
        route='solicitudes-etp',
        view= views.solicitudesETP,
        name= 'solicitudesETP'
    ),
    path(
        route='validar-etp',
        view= views.validarETP,
        name= 'validarETP'
    ),
    path(
        route='ver-historial-etps',
        view= views.historialETP,
        name= 'historialETP'
    ),
    path(
        route='ver-equipos',
        view= views.verEquipos,
        name= 'verEquipos'
    ),
    path(
        route='crear-equipos',
        view= views.crearEquipos.as_view(),
        name= 'crearEquipos'
    ),

    #ETP
    path(
        route='crear-etp',
        view=views.etpCrear,
        name='etpCrear'
    ),
    path(
        route='etp-en-proceso',
        view=views.etpProceso,
        name='etpProceso'
    ),
    path(
        route='solicitudes-etp-uteycv',
        view=views.etpSolicitudes,
        name='etpSolicitudes'
    ),
    #Evaluador UPEV
    path(
        route='tablero-actividades',
        view=views.tableroActividades,
        name='tableroActividades'
    ),
    path(
        route='actividades-pasadas',
        view=views.pasadasActividades,
        name='pasadasActividades'
    ),
    path(
        route='admin',
        view = views.test_admin,
        name='admin'
    ),
    path(
        route='uteycv',
        view = views.test_uteycv,
        name='uteycv'
    ),
    path(
        route='evaluador',
        view = views.test_evaluador,
        name='evaluador'
    ),
    path(
        route='cambiarEstadoETP',
        view= views.cambiarEstadoETP,
        name='cambiarEstadoETP'
    )
    

]


