from django.urls import path
from . import views

urlpatterns = [
    path('', views.register, name="register"),
    path('fill/', views.fill, name="fill"),
]