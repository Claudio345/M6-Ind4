from django.contrib import admin
from . models import Categoria, Usuario

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    
class UsuarioAdmin(admin.ModelAdmin):
    exclude = ('create_at', )
    list_display = ('id','imagen','nombre', 'telefono', 'email', 'create_at')
    

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Usuario, UsuarioAdmin)