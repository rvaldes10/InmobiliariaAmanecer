from django.db import models

# Create your models here.
class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nombreCompleto = models.CharField(max_length=50)
    mail = models.EmailField()
    telefono = models.IntegerField()
    class Meta:
        db_table = "cliente"

class Galeria(models.Model):
    id_imagen = models.AutoField(primary_key=True)
    imagen = models.ImageField(null = True)
    class Meta:
        db_table = "galeria"