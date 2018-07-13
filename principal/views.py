from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404

# en esta app voy a poner settings, pagina principal y cosillas que aparezcan
# continuamente en la pantalla a pesar de estar en otras apps


def hola(request):

    return render(request, 'hola.html')

def contacta(request):

    return render(request, 'contacta.html')

def funciona(request):

    return render(request, 'funciona.html')