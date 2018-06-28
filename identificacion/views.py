from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.forms import modelformset_factory
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


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
            try:
                user.save()
            except:
                Http404("error al save el user")
            try:
                user = authenticate(request, username=username, password= password)
                if user is not None:
                    login(request, user)
                else:
                    Http404("ha fallado el login")
            except:
                Http404("ha fallado el loop try del authenitcate")
            try:
                d=DataSheet.objects.get(username=username)
            except:
                return HttpResponseRedirect('/identificacion/fill')
            else:
                Http404("estas ya metido y rellenado")
        if request.POST.get("login"):
            user1 = request.POST.get("name1")
            password1 = request.POST.get("password1")
            user = authenticate(request, username=user1, password= password1)
            if user is not None:
                login(request, user)
                try:
                    d = DataSheet.objects.get(username=user1)
                except:
                    return HttpResponseRedirect('/usuario/')
                else:
                    return HttpResponseRedirect('')
            else:
                raise Http404("no auth")

    return render(request, 'register.html')

