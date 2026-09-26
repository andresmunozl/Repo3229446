from rest_framework.viewsets import ModelViewSet
from granja.api.serializers import AnimalSerializer
from granja.models import Animal


class AnimalViewSet(ModelViewSet):
    serializer_class = AnimalSerializer
    queryset = Animal.objects.all()
    