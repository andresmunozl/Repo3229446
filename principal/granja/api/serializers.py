from rest_framework import serializers
from granja.models import Animal


class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = ['id', 'nombre', 'especie', 'edad', 'saludable']
        
        