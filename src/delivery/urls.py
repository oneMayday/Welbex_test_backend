from django.urls import include, path

from rest_framework.routers import DefaultRouter

from delivery.views import CargoAPIView, DeliveryCarAPIView, LocationAPIView


router = DefaultRouter()
router.register('deliverycar', DeliveryCarAPIView, basename='deliverycar')
router.register('cargo', CargoAPIView, basename='cargo')
router.register('location', LocationAPIView, basename='location')

urlpatterns = [
    path('', include(router.urls)),
]
