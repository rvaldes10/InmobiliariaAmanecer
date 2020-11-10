from django.db import models

# Create your models here.
class Cliente(models.Model):
    RUT = models.CharField(primary_key=True)
    NombreCompleto = models.CharField(max_length=50)
    mail = models.EmailField()
    telefono = models.IntegerField(max_length=10)

class Meta:
    db_table = 'cliente'