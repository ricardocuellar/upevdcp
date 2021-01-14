"""upevdcp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render, redirect
from django.conf import settings
from django.conf.urls.static import static
from comentarios.views import home,verComentario,upload_file_view, upload_image_view
from django.views.decorators.csrf import csrf_exempt


from django.http import HttpResponse

def root_to_dashboard(request):
     return redirect('/dashboard')

urlpatterns = [

    #Root
    path('', root_to_dashboard),
    #Admin panel
    path('admin/', admin.site.urls),
    
    #Login System
    path('users/',include(('users.urls','users'),namespace = 'users')),

    #Dashboard
    path('dashboard/',include(('dashboard.urls','dashboard'), namespace = 'dashboard')),

    #Uploads
    path('fileUPload/',csrf_exempt(upload_file_view)),
    path('imageUPload/',csrf_exempt(upload_image_view)),

    #Comentarios
    path('editorComentarios/',home),
    path('comentario/<int:comentarioID>/',verComentario),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
