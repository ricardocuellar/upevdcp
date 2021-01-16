from django.shortcuts import render, redirect
from django.views.decorators.csrf import requires_csrf_token
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse
from django.utils import timezone
from comentarios.forms import ComentarioForm
from comentarios.models import Comentario
from etps.models import ETP
# Create your views here.

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







@requires_csrf_token
def upload_image_view(request):
    f= request.FILES['image']
    fs = FileSystemStorage()
    filename = str(f).split('.')[0]
    file = fs.save(filename,f)
    fileurl = fs.url(file)
    return JsonResponse({'success':1, 'file':{'url':fileurl}})


@requires_csrf_token
def upload_file_view(request):
    f= request.FILES['file']
    fs = FileSystemStorage()
    filename,ext=str(f).split('.')
    print(filename)
    file = fs.save(filename+'.'+ext,f)
    print(file)
    fileurl = fs.url(file)
    return JsonResponse({'success':1,
    'file': 
    {'url':fileurl, "size": fs.size(file), "name": str(f), "extension": ext}
    })



def verTablaComentarios(request,etpID):
    comentarios = Comentario.objects.filter(etp_id=etpID)
    etp = ETP.objects.get(id=etpID)
    return render(request,'comentario/verTablaComentarios.html',{'comentarios':comentarios, 'etp':etp})

def confirmarCorreccion(request, etpID, comentarioID):
    comentarios = Comentario.objects.get(id=comentarioID)
    etp = ETP.objects.get(id=etpID)
    comentarios.revisado = 1
    etp.pendientes = 0
    comentarios.save()
    etp.save()

    return redirect('/dashboard/tablaComentarios/'+str(etpID))

