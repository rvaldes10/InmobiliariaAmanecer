from django.shortcuts import render, redirect
from AppInmobiliariaAmanecer.forms import ClienteForm
from AppInmobiliariaAmanecer.models import Cliente

# Create your views here.

#def clientes(request):
 #   if request.method == 'POST':
  #      form = ClienteForm(request.POST)
   #     if form.is_valid():
    #        try:
     #           form.save()
      #          return redirect('/home')
       #     except:
        #        pass
    #else:
     #   form = ClienteForm()
        #clientes = Cliente.objects.all()
    #return render(request,'registro.html',{'from' : form, 'clientes' : clientes})

    