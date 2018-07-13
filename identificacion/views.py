from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from usuario.models import Comentarios
from usuario.models import Asignaturas
from django.db import IntegrityError

def login(request):
    if request.method=='POST':
        username=request.POST.get('name')
        password=request.POST.get('password')
        try:
            user=authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/usuario')
            else:
                raise Http404("ERROR interno")
        except:
            raise Http404("ERROR contraseña o usuario")

    return render(request, 'login.html')

def registrar(request):
    if request.method=='POST':
        username=request.POST.get('name')
        password=request.POST.get('password')
        email=request.POST.get('email')
        try:
            user=User.objects.create_user(username=username, password=password, email=email)
        except:
            raise Http404("Nombre cogido")
        try:
            user.save()
        except:
            raise Http404("Error interno")
        try:
            d=Comentarios(username=username)
            d.save()
        except:
            raise Http404("error comentarios")
        try:
            m=Asignaturas(username=username)
            if request.POST["matematicas"]:
                m.matematicas="t"
            if request.POST["fisica"]:
                m.fisica="t"
            if request.POST["quimica"]:
                m.quimica="t"
            m.save()
        except:
            raise Http404("error asignaturas")
        try:
            user=authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/usuario')
            else:
                raise Http404("ERROR interno")
        except:
            raise Http404("ERROR interno")

    return render(request, 'register.html')