from django.urls import path
from . import views
#* llego con esta base http://127.0.0.1:8000/usuarios/
app_name = 'usuario' # asegurarme que exista el namespace 
urlpatterns = [
    path('',views.index, name='index'), #* llego con esta base http://127.0.0.1:8000/usuarios/
    path('formulario/', views.formulario, name='formulario'), #* llego con esta base http://127.0.0.1:8000/usuarios/formulario/
    path('<int:usuario_id>', views.detail, name="detail"),
    path('<int:usuario_id>/eliminar/', views.eliminar_usuario, name="eliminar"),
    path('<int:usuario_id>/editar/', views.editar_usuario, name='editar')
]
