from django.contrib import admin
from usuario.models import Comentarios

class ComentariosAdmin(admin.ModelAdmin):
    pass
admin.site.register(Comentarios, ComentariosAdmin)