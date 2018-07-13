from django.contrib import admin
from usuario.models import Comentarios
from usuario.models import Asignaturas

class ComentariosAdmin(admin.ModelAdmin):
    pass
admin.site.register(Comentarios, ComentariosAdmin)

class AsignaturasAdmin(admin.ModelAdmin):
    pass
admin.site.register(Asignaturas, AsignaturasAdmin)