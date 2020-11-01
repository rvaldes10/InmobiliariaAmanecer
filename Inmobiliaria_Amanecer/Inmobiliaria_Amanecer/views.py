from django.http import HttpResponse
from django.template import Template, context, loader

def Home(request):
    
    home = loader.get_template('index.html')
    pagina = home.render()

    return HttpResponse(pagina)

def Registro(request):
    
    registro = loader.get_template('registro.html')
    pagina = registro.render()

    return HttpResponse(pagina)

def MasterPlan(request):
    
    masterplan = loader.get_template('masterplan.html')
    pagina = masterplan.render()

    return HttpResponse(pagina)