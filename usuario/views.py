from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.forms import modelformset_factory
from django import forms
from django.contrib.auth.models import User
from usuario.models import Comentarios
from django.contrib.auth import authenticate, login

def inicio(request):
    if request.method=='GET':
        username=None
        score_text=None
        horario_text=None
        if request.user.is_authenticated:
            username=request.user.username
            try:
                score_text=Comentarios.objects.values_list('score_text', flat=True).get(username=username)
                horario_text=Comentarios.objects.values_list('horario_text', flat=True).get(username=username)
                if score_text == ' ':
                    score_text="Vaya, todavía no tienes un seguimiento. Contacta con nosotros por correo o móvil y trabajaremos en él."
                if horario_text == ' ':
                    horario_text="Vaya, todavía no tienes un horario. Contacta con nosotros por correo o móvil y trabajaremos en él."
            except:
                score_text="Vaya, parece que ha habido un error. Por favor, háznoslo saber contactando con nosotros por correo o móvil."
                horario_text="Vaya, parece que ha habido un error. Por favor, háznoslo saber contactando con nosotros por correo o móvil."

        else:
            Http404("Ha ocurrido un error en la identificación del usuario.")

    context={'score_text':score_text, 'horario_text':horario_text,'username':username}
    return render(request, 'inicio.html', context)
