from django.shortcuts import render, redirect
from AppInmoAmanecer.forms import ClienteForm
from AppInmoAmanecer.models import Cliente

# Create your views here.

def clientes(request):
    l_clientes = Cliente.objects.all()
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/registro')
            except:
                pass
    else:
        form = ClienteForm()
    return render(request, 'registro.html',{'form': form, 'clientes': l_clientes})

#Listar Clientes

def Listar(request):
   l_clientes = Cliente.objects.all()
   for cli in l_clientes:
    return {{cli.nombre}}, {{cli.id_cliente}}, {{cli.telefono}}, {{cli.mail}}

#Modificar Clientes

def modificar(request,id):
   cli = Cliente.objects.get(id_cliente = id)
   form = ClienteForm(instance=cli)
   return render(request,'edit.html', {'form': form, 'id_cliente': cli.id_cliente})

#Eliminar Clientes