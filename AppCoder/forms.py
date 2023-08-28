from django import forms 

class AulaForm(forms.Form):
    nombre=forms.CharField(max_length=50)
    comision=forms.IntegerField()
    
class TutorForm(forms.Form):
    nombre=forms.CharField(max_length=50)
    apellido=forms.CharField(max_length=50)
    email=forms.EmailField()
    profesion=forms.CharField(max_length=50)
    
class EstudianteForm(forms.Form):
    nombre=forms.CharField(max_length=50)
    apellido=forms.CharField(max_length=50)
    email=forms.EmailField()
    

class DesafioForm(forms.Form):
    nombre=forms.CharField(max_length=50)
    fecha_entrega=forms.DateField()
    entregado=forms.BooleanField() 