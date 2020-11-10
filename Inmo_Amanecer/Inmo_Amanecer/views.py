from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def registro(request):
    return render(request, 'registro.html')

def masterplan(request):
    return render(request, 'masterplan.html')
