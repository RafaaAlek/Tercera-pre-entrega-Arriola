from django.urls import path
from AppCoder.views import *

urlpatterns = [
   
    path('agregar-producto/<nombre>/<cantidad>', producto),
    path('lista-productos/', lista_productos),
    path('lista-categorias/', lista_categorias),
    path('lista-clientes/', lista_clientes),
    path('', Inicio, name='Inicio'),
    path('categorias/', Categorias, name='Categorias'),
    path('productos/', Productos, name='Productos'),
    path('clientes/', Clientes, name='Clientes'),
    path('categoria-fomulario/', Categoria_formulario, name='Categoriaformulario'),
    path('producto-fomulario/', Producto_formulario, name='Productoformulario'),
    path('cliente-fomulario/', Cliente_formulario, name='Clienteformulario'),
    path('busqueda-apellido/', busqueda_apellido, name='busquedaApellido'),
    path('buscar/', buscar, name='Buscar'),


]