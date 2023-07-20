from django.shortcuts import render
from aplicacion_1.models import registroUsuarios


def primeraFuncion(request):
    return render(request, 'landing.html')


def formularioContacto(request):
    return render(request, 'registro.html')


def informeUsuarios(request):
     #'usuarios' es una instancia de la clase "registroUsuarios" definida en models.py
    usuarios = registroUsuarios.objects.all()
    #data = {
    #    'usuarios': usuarios
    #}
    return render(request, 'salida.html', {'usuarios': usuarios})