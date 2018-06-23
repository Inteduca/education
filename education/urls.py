from django.urls import path, include
from django.contrib import admin
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView

urlpatterns = [
    path('principal/', include('principal.urls')),
    path('identificacion/', include('identificacion.urls')),
    path('admin/', admin.site.urls),
]
