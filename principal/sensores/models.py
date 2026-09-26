from django.db import models


class Sensor(models.Model):

    TIPO_CHOICES = [
        ('TEMP', 'Temperatura'),
        ('HUM', 'Humedad'),
        ('AMON', 'Amoníaco'),
        ('PESO', 'Peso'),
    ]

    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    ubicacion = models.CharField(max_length=100)
    valor_actual = models.DecimalField(max_digits=6, decimal_places=2)
    unidad_medida = models.CharField(max_length=20)
    activo = models.BooleanField(default=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} ({self.tipo})"


