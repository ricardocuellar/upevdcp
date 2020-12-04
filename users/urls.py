"""Users URLs"""

#Django
from django.urls import path
from django.views.generic import TemplateView

# Views 
from users import views

urlpatterns = [
    
    #Management
    path(
        route='login/', 
        view=views.LoginView.as_view(redirect_authenticated_user = True),
        name='login'
        ),

]
