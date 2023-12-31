from django.db import models

# Create your models here.
class Aula(models.Model):
    nombre=models.CharField(max_length=50)
    comision=models.IntegerField()
    def __str__(self):
        return f"{self.nombre} - {self.comision}"


class Estudiante(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    email=models.EmailField()
    def __str__(self):
        return f"{self.nombre} - {self.apellido}"
    


class Tutor(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    email=models.EmailField()
    profesion=models.CharField(max_length=50)
    def __str__(self):
        return f"{self.nombre} - {self.apellido}"

    
class Desafio(models.Model):
    nombre=models.CharField(max_length=50)
    fecha_entrega=models.DateField()
    entregado=models.BooleanField()
    def __str__(self):
        return f"{self.nombre} - {self.fecha_entrega} - {self.entregado}"    
    
    