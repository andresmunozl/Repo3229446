from rest_framework import serializers
from sensores.models import Sensor


class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = [
            'id', 'nombre', 'tipo', 'ubicacion',
            'valor_actual', 'unidad_medida', 'activo', 'fecha_registro'
        ]
        read_only_fields = ['fecha_registro']
        