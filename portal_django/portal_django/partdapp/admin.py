from django.contrib import admin
from . import models
    
class CategoriaAdmin(admin.ModelAdmin):
    list_display=("materia",)

class AnunciosAdmin(admin.ModelAdmin):
    list_display=("id", "nombre", "telefono", "email", "categoria", "emailvalido")
    search_fields=("nombre", "telefono", "email")
    list_filter=("emailvalido", "categoria")
    
class UsuariosAdmin(admin.ModelAdmin):
    list_display=("id", "email")
    
class ChatAdmin(admin.ModelAdmin):
    list_display=("nom", "mensaje")
    
admin.site.register(models.Categoria, CategoriaAdmin)
admin.site.register(models.Usuarios, UsuariosAdmin)
admin.site.register(models.Anuncio, AnunciosAdmin)
admin.site.register(models.Chat, ChatAdmin)
