from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404

# en esta app voy a poner settings, pagina principal y cosillas que aparezcan
# continuamente en la pantalla a pesar de estar en otras apps


def principal(request):

    return render(request, 'principal.html')

def who (request):

    return render(request, 'who.html')

def ayuda (request):

    return render(request, 'ayuda.html')

def ajustes (request):

    return render(request, 'ajustes.html')

def contacta (request):

    return render(request, 'contacta.html')