from django.shortcuts import render
from django.template import Template, context, loader

def index(request):
    return render(request, 'index.html')

def registro(request):
    return render(request, 'registro.html')

def masterplan(request):
    return render(request, 'masterplan.html')
