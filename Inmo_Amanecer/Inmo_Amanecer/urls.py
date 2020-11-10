"""Inmo_Amanecer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Inmo_Amanecer.views import index, registro, masterplan

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index),
<<<<<<< HEAD
    path('registro/', views.clientes),
    path('masterplan/', masterplan),
    path('edit/<int:id>', views.modificar),
=======
    path('registro/', registro),
    path('masterplan/', masterplan)
>>>>>>> parent of bf645d5... Conexion y migracion de modelos con BD
]
