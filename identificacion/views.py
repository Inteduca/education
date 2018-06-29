from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from usuario.models import Comentarios
from django.db import IntegrityError

def register(request):
    #diferenciar los botones y decir si e presiona uno hace x
    #si se presiona otro hace y
    if request.method=='POST':
        if request.POST.get("register"):
            username=request.POST.get('name')
            password=request.POST.get('password')
            email=request.POST.get('email')
            user=User.objects.create_user(username=username, password=password, email=email)
            #es necesario meter asi los users en la db si quieres que luego funcionen con los auth etc
            try: #salvar al user
                user.save()
            except:
                raise Http404("Vaya, parece que ha ocurrido un error. Prueba con otro nombre de usuario, o contacta con nosotros.")
            try: #hacer un comentarios
                d=Comentarios(username=username)
                d.save()
            except:
                raise Http404("Vaya, parece que ha ocurrido un error, y ¡es nuestra culpa! Por favor, háznoslo saber contactando con nosotros por correo o móvil")
            try:
                user = authenticate(request, username=username, password= password)
                if user is not None:
                    login(request, user)
                    return HttpResponseRedirect('/usuario/')
                else:
                    raise Http404("Vaya, parece que ha ocurrido un error, y ¡es nuestra culpa! Por favor, háznoslo saber contactando con nosotros por correo o móvil")
            except:
                raise Http404("Vaya, parece que ha ocurrido un error, y ¡es nuestra culpa! Por favor, háznoslo saber contactando con nosotros por correo o móvil")

        if request.POST.get("login"):
            user1 = request.POST.get("name1")
            password1 = request.POST.get("password1")
            user = authenticate(request, username=user1, password= password1)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/usuario/')
            else:
                raise Http404("¡Vaya! Parece que la contraseña es incorrecta. Asegúrate de escribirla bien y, si lo necesitas, contacta con nosotros por correo o móvil")
    return render(request, 'register.html')

