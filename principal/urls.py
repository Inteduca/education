from django.urls import path
from . import views

urlpatterns = [
    path('', views.principal, name="principal"),
    path('ajustes', views.ajustes, name="ajustes"),
    path('who', views.who, name="who"),
    path('ayuda', views.ayuda, name="ayuda"),
    path('contacta', views.contacta, name="contacta"),
]