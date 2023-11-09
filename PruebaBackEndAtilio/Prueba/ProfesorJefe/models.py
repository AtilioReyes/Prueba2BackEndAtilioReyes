from django.db import models

class ProfJefe(models.Model):
    nombre = models.CharField(max_length=40)
    edad = models.CharField(max_length=2)
    asignatura = models.CharField( max_length=30)
    rut = models.CharField(max_length=12)
    correo = models.CharField(max_length=100)
    horario = models.CharField(max_length= 40)
    


# Create your models here.
