from django.urls import path
from AppCoder.views import *

urlpatterns = [
   
    path('agregar-producto/<nombre>/<cantidad>', producto),
    path('lista-productos/', lista_productos),
    path('', Inicio, name='Inicio'),
    path('categorias/', Categorias, name='Categorias'),
    path('productos/', Productos, name='Productos'),
    path('clientes/', Clientes, name='Clientes'),
    path('categoria-fomulario/', Categoria_formulario, name='Categoriaformulario'),
    path('cliente-fomulario/', Cliente_formulario, name='Clienteformulario'),
    path('busqueda-apellido/', busqueda_apellido, name='busquedaApellido'),
    path('buscar/', buscar, name='Buscar'),


]