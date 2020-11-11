from django import forms
from AppInmobiliariaAmanecer.models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = "__all__"