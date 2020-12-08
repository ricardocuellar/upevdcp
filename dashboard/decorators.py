from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse
from django.core.exceptions import PermissionDenied
from users.models import UsersRole
from django.shortcuts import redirect


def admin_required(function):
    def is_admin(request):
        print(request)
        user_id = request.pk
        rol = UsersRole.objects.get(user_id=user_id).role 
        return rol  == "admin"
       
    actual_decorator = user_passes_test(is_admin)
    if function:
        return actual_decorator(function)
    else:
        return redirect('/dashboard')



def uteycv_required(function):
    def is_uteycv(request):
        user_id = request.pk
        rol = UsersRole.objects.get(user_id=user_id).role 
        return rol  == "uteycv"
    actual_decorator = user_passes_test(is_uteycv)
    if function:
        return actual_decorator(function)
    else:
        return redirect('/dashboard')


def evaluador_required(function):
    def is_evaluador(request):
        user_id = request.pk
        rol = UsersRole.objects.get(user_id=user_id).role 
        return rol  == "evaluador"
    actual_decorator = user_passes_test(is_evaluador)
    if function:
        return actual_decorator(function)
    else:
        return redirect('/dashboard')