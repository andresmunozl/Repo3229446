from rest_framework.routers import DefaultRouter
from .views import SensorViewSet

router_sensor = DefaultRouter()
router_sensor.register(prefix="sensores", viewset=SensorViewSet, basename="sensores")

urlpatterns = router_sensor.urls