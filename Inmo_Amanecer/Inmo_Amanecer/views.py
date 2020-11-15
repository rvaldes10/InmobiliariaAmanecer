from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def masterplan(request):
    return render(request, 'masterplan.html')
