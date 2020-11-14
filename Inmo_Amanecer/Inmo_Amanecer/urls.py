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
from django.urls import path, include
from Inmo_Amanecer.views import index, masterplan
from AppInmobiliariaAmanecer.views import CotizacionCliente, listar_clientes, \
    modificar_cliente, eliminar_cliente
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index, name="Index"),
    path('masterplan/', masterplan, name="Master_Plan"),
    path('cotizacion_cliente/', CotizacionCliente, name="Cotizacion_Cliente" ),
    path('listar_clientes/', listar_clientes, name="Listar_Cliente"),
    path('listar_clientes/modificar_cliente/<int:id>/', modificar_cliente, name="Modificar_Cliente"),
    path('listar_clientes/eliminar_cliente/<int:id>/', eliminar_cliente, name="Eliminar_Cliente"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('recuperar_contraseña/', auth_views.PasswordResetView.as_view(template_name='registration/reset_passwd.html'), name="Recuperar_Contraseña"),
    path('recuperar_contraseña/', auth_views.PasswordResetDoneView.as_view(template_name='registration/reset_passwd_sended.html'), name="Recuperar_Contraseña_Enviado"),
    path('recuperar_contraseña/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/reset_passwd_form.html'), name="Recuperar_Contraseña_Formulario"),
    path('recuperar_contraseña/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/reset_passwd_ready.html'), name="Recuperar_Contraseña_Enviado"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
