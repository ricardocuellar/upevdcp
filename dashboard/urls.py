"""Dashboard URLs"""

#Django
from django.urls import path
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from comentarios.views import home,verComentario,upload_file_view, upload_image_view, verTablaComentarios, confirmarCorreccion
from django.views.decorators.csrf import csrf_exempt
# Views 
from dashboard import views
from dashboard.views import reanudarTarea, descargarUltimoReporte

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
    ),

    #Tarea estados
    path('reanudarTarea/<int:tareaID>/<int:etpID>', reanudarTarea, name='reanudarTarea'),

     #Uploads
    path('fileUPload/',csrf_exempt(upload_file_view)),
    path('imageUPload/',csrf_exempt(upload_image_view)),

    #Comentarios
    path('editorComentarios/',home),
    path('tablaComentarios/<int:etpID>/', verTablaComentarios, name='tablaComentarios'),
    path('tablaComentarios/confirmarCorrecciones/<int:etpID>/<int:comentarioID>', confirmarCorreccion, name='confirmarCorreccion'),
    path('comentario/<int:comentarioID>/',verComentario, name='verComentario'),
    
    #Admins descargar última versión
    path('descargar/ultimoReporte/<int:etpID>/', descargarUltimoReporte, name='descargarUltimoReporte'),
    

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


