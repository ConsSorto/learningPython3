from django.shortcuts import render, HttpResponse

def HolaMundo(request):
    return HttpResponse("<h1>Hola Mundo</h1>"+
        "<h3>esto es Django con CONS SORTO</h3>")


def HolaMundo2(request, nombre):
    return HttpResponse(f"<h1>Hola Mundo {nombre}</h1>"+
        "<h3>esto es Django con CONS SORTO</h3>")

# Create your views here.
