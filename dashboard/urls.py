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
        route='solicitudes-etp',
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
    

]
