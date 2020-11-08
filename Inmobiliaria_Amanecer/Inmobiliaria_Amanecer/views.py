from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,get_object_or_404
from django.template import Template, context, loader, RequestContext

#def Home(request):
    
    #home = Home.objects.all()
    #return render('index.html', {'home':home}, context_instance=RequestContext(request))

def Registro(request):
    
    registro = loader.get_template('registro.html')
    pagina = registro.render()

    return HttpResponse(pagina)

def MasterPlan(request):
    
    masterplan = loader.get_template('masterplan.html')
    pagina = masterplan.render()

    return HttpResponse(pagina)