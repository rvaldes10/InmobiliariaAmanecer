from django.shortcuts import render, redirect
from AppInmoAmanecer.forms import ClienteForm
from AppInmoAmanecer.models import Cliente

# Create your views here.

def clientes(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/cotizacionclientes')
            except:
                pass
    else:
        form = ClienteForm()
        #clientes = Cliente.objects.all()
    return render(request, 'registro.html',{'form': form, 'clientes': clientes})