from django.db import models

# Create your models here.

class Cliente(models.Model):
    
    id_cliente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    mail = models.EmailField()
    telefono = models.IntegerField()

    def __str__(self):
        return self.nombre

class Meta:
    db_table = "cliente"