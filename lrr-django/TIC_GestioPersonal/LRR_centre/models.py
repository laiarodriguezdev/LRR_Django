from django.db import models

# Create your models here.

class Rol(models.Model):
    id= models.CharField(primary_key=True)
    nom = models.CharField(max_length=100)
    
    def __str__(self):
        return f'{self.id} {self.nom}'

class Usuari(models.Model):
    id= models.CharField(primary_key=True)
    nom = models.CharField(max_length=100)
    cognom = models.CharField(max_length=100)
    edat = models.CharField(max_length=100)
    correu = models.CharField(max_length=100)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)
    assignatures = models.CharField(max_length=200)
    
    def __str__(self):
        return f'{self.id} {self.nom} {self.cognom} {self.edat} {self.correu} {self.rol} {self.assignatures}'