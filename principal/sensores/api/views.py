from rest_framework.viewsets import ModelViewSet
from sensores.api.serializers import SensorSerializer
from sensores.models import Sensor


class SensorViewSet(ModelViewSet):
    serializer_class = SensorSerializer
    queryset = Sensor.objects.all()