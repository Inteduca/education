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
            except:
                score_text="error, mande un mail o un mensaje"
                horario_text="error, mande un mail o un mensaje"

        else:
            Http404("usuario no identificado")

    context={'score_text':score_text, 'horario_text':horario_text,'username':username}
    return render(request, 'inicio.html', context)
