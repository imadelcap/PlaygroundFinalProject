from django.db import models

# Reutilizo modelos de entrega, pero solo de tipo stock.

class ModeloBicicleta(models.Model):
    marca = models.CharField(max_length=20)
    tipo = models.CharField(max_length=30)
    rodado = models.IntegerField()
    stock = models.IntegerField()
    creado = models.DateTimeField(null=True)
    modificado = models.DateTimeField(null=True)

    def __str__(self):
        return (
            'Bicicleta: ' + self.marca + 
            ' - ' + self.tipo + 
            ' - rodado ' + self.rodado + 
            ' - stock ' + self.stock +
            'Creado: ' + self.creado +
            'Modificado: ' + self.modificado
        )
            

class Accesorio(models.Model):
    tipo = models.CharField(max_length=20) 
    marca = models.CharField(max_length=20)
    descripcion = models.TextField(max_length=100)
    stock = models.IntegerField()
    creado = models.DateTimeField(null=True)
    modificado = models.DateTimeField(null=True)
    
    def __str__(self):
        return (
            'Accesorio: ' + self.tipo + 
            ' - ' + self.marca + 
            ' - ' + self.descripcion + 
            ' - stock ' + self.stock +
            'Creado: ' + self.creado +
            'Modificado: ' + self.modificado
        )