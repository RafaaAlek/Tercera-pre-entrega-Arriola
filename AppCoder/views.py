from django.http import HttpResponse
from django.shortcuts import render
from .models import Producto

# Create your views here.
def producto(req, nombre, cantidad):

    producto = Producto(nombre=nombre, cantidad=cantidad)
    producto.save()

    return HttpResponse (f"""
        <p>Producto: {producto.nombre} - Cantidad {producto.cantidad} agregado!</p>
    """)

def lista_productos(req):

    lista = Producto.objects.all()

    return render(req, "lista_productos.html", {"lista_cursos": lista})
