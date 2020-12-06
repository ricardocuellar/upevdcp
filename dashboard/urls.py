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
        view=views.DashboardView.as_view(),
        name='dashboard'
        ),
    

]
