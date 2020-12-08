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
