from django.urls import path
from . import views

urlpatterns = [
    path('', views.hola, name="hola"),
    path('contacta', views.contacta, name="contacta"),
    path('como_funciona', views.funciona, name="funciona")
]