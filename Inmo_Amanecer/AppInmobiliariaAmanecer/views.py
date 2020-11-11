from django.shortcuts import render, redirect
from AppInmobiliariaAmanecer.forms import ClienteForm
from AppInmobiliariaAmanecer.models import Cliente

# Create your views here.

def RegistroCliente(request):

    data = {

        'form': ClienteForm()

    }

    if request.method == 'POST':

        formulario = ClienteForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "¡Solicitud de Cotizacion Enviada!"
        else:
            data["form"] = formulario

    return render(request, 'registro.html', data)

