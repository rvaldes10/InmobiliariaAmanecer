from django.db import models

# Create your models here.

class Cliente(models.Model):
    
    RUT = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    mail = models.EmailField()
    telefono = models.IntegerField()

class Meta:
    db_table = "cliente"