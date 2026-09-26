from rest_framework.routers import DefaultRouter
from .views import AnimalViewSet

router_granja = DefaultRouter()
router_granja.register(prefix="granja", viewset=AnimalViewSet, basename="granja")

urlpatterns = router_granja.urls