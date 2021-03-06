from django.shortcuts import render, redirect, get_object_or_404
from AppInmobiliariaAmanecer.forms import ClienteForm
from AppInmobiliariaAmanecer.models import Cliente, Galeria
from django.contrib.auth.decorators import login_required

# Create your views here.

def CotizacionCliente(request):

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

    return render(request, 'cotizacion.html', data)

@login_required(login_url='login')
def listar_clientes(request):

    clientes = Cliente.objects.all()

    data = {

        'clientes': clientes

    }

    return render(request, 'Listar.html', data)

@login_required(login_url='login')
def modificar_cliente(request, id):

    cliente = get_object_or_404(Cliente, id_cliente=id)

    data = {

        'form': ClienteForm(instance=cliente)

    }

    if request.method == 'POST':
        formulario =  ClienteForm(data=request.POST, instance=cliente)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="Listar_Cliente")
        data["form"] = formulario

    return render(request, 'Modificar.html', data)

@login_required(login_url='login')
def eliminar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id_cliente=id)
    cliente.delete()
    return redirect(to="Listar_Cliente")

