from django.http import HttpResponse
from django.shortcuts import render
from .models import Producto, Cliente, Categoria
from .forms import Categoriaformulario, Clienteformulario

# Create your views here.
def producto(req, nombre, cantidad):

    producto = Producto(nombre=nombre, cantidad=cantidad)
    producto.save()

    return HttpResponse (f"""
        <p>Producto: {producto.nombre} - Cantidad {producto.cantidad} agregado!</p>
    """)

def lista_productos(req):

    lista = Producto.objects.all()

    return render(req, "lista_productos.html", {"lista_productos": lista})


def Inicio(req):

    return render(req, "inicio.html")
    

def Categorias(req):

    return render(req, "categorias.html")

def Productos(req):

    return render(req, "productos.html")

def Clientes(req):

    return render(req, "clientes.html")

def Categoria_formulario(req):

    if req.method == 'POST':

        miFormulario = Categoriaformulario(req.POST)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data

            categoria = Categoria(nombre=data["nombre"])
            categoria.save()
            return render(req, "inicio.html", {"mensaje": "Categoria ingresada con exito"})
        else:
            return render(req, "inicio.html", {"mensaje": "Formulario invalido"})
    else:

        miFormulario = Categoriaformulario()

        return render(req, "categoria_fomulario.html", {"miFormulario": miFormulario})


def Cliente_formulario(req):

    if req.method == 'POST':

        miFormulario = Clienteformulario(req.POST)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data

            cliente = Cliente(nombre=data["nombre"], apellido=data["apellido"], email=data["email"])
            cliente.save()
            return render(req, "inicio.html", {"mensaje": "Cliente ingresado con exito"})
        else:
            return render(req, "inicio.html", {"mensaje": "Formulario invalido"})
    else:

        miFormulario = Clienteformulario()

        return render(req, "cliente_fomulario.html", {"miFormulario": miFormulario})

def busqueda_apellido(req):

    return render(req, "busquedaApellido.html")

def buscar(req):

    if req.GET["apellido"]:
        apellido = req.GET["apellido"]
        nombres = Cliente.objects.filter(apellido__icontains=apellido)
        if nombres:
            return render(req, "resultadoBusqueda.html", {"nombres": nombres})
    else:
        return HttpResponse('No escribiste Apellido')
