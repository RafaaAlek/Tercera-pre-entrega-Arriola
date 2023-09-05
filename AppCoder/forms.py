from django import forms

class Clienteformulario(forms.Form):

    nombre = forms.CharField(required=True)
    apellido = forms.CharField(required=True)
    email = forms.EmailField(required=True)

class Categoriaformulario(forms.Form):

    nombre = forms.CharField(required=True)

class Productoformulario(forms.Form):

    nombre = forms.CharField(required=True)
    cantidad = forms.IntegerField()


    