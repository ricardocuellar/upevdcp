from django.shortcuts import render
from django.views.decorators.csrf import requires_csrf_token
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse
from django.utils import timezone
from comentarios.forms import ComentarioForm
from comentarios.models import Comentario
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
    file = fs.save(filename+'.'+ext,f)
    fileurl = fs.url(file)
    return JsonResponse({'success':1,
    'file': 
    {'url':fileurl, "size": fs.size(filename), "name": str(f), "extension": ext}
    })
