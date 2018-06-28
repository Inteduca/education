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
            except IntegrityError:
                messages.add_message(request, messages.INFO, 'Ese nombre de usuario ya está escogido.')
            except:
                Http404("Vaya, parece que ha ocurrido un error, y ¡es nuestra culpa! Por favor, háznoslo saber contactando con nosotros por correo o móvil")
            try: #hacer un comentarios
                d=Comentarios(username=username)
                d.save()
            except:
                Http404("Vaya, parece que ha ocurrido un error, y ¡es nuestra culpa! Por favor, háznoslo saber contactando con nosotros por correo o móvil")
            try:
                user = authenticate(request, username=username, password= password)
                if user is not None:
                    login(request, user)
                    return HttpResponseRedirect('/usuario/')
                else:
                    Http404("Vaya, parece que ha ocurrido un error, y ¡es nuestra culpa! Por favor, háznoslo saber contactando con nosotros por correo o móvil")
            except:
                Http404("Vaya, parece que ha ocurrido un error, y ¡es nuestra culpa! Por favor, háznoslo saber contactando con nosotros por correo o móvil")

        if request.POST.get("login"):
            user1 = request.POST.get("name1")
            password1 = request.POST.get("password1")
            user = authenticate(request, username=user1, password= password1)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/usuario/')
            else:
                messages.add_message(request, messages.INFO, 'Nombre de usuario y contraseña no coinciden. ¿Te has olvidado de la contraseña? Contacta con nosotros por correo o móvil.')

    return render(request, 'register.html')

