from django.urls import path, include
from django.contrib import admin
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView

urlpatterns = [
    path('', include('principal.urls')),
    path('inicio/', include('principal.urls')),
    path('identificacion/', include('identificacion.urls')),
    path('usuario/', include('usuario.urls')),
    path('admin/', admin.site.urls),
]
