from django.shortcuts import render
from .forms import AspiranteForm
from django.contrib import messages

# Create your views here.

def home(request):
    return render (request, 'app/home.html')

def galeria(request):
    return render (request, 'app/galeria.html')


def quienes_somos(request):
    return render (request, 'app/quienes_somos.html')

def registrate(request):
    data = {
        'form': AspiranteForm()
    }

    if request.method == 'POST':
        formulario = AspiranteForm(data=request.POST)
        if formulario.is_valid():

            formulario.save()
            messages.success(request, 'Registro Exitoso')

        else:
            data["form"] = formulario


    return render (request, 'app/registrate.html',data)
