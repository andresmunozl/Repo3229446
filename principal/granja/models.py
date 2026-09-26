from django.db import models


class Animal(models.Model):
    nombre = models.CharField(max_length=100)
    especie = models.CharField(max_length=100)
    edad = models.PositiveIntegerField(default=0)
    saludable = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre
    
    