from django.urls import include, path

from rest_framework.routers import DefaultRouter

from delivery.views import DeliveryCarUpdateAPIView, CargoAPIView


router = DefaultRouter()
router.register('deliverycar', DeliveryCarUpdateAPIView, basename='deliverycar')
router.register('cargo', CargoAPIView, basename='cargo')

urlpatterns = [
    path('', include(router.urls)),
]
