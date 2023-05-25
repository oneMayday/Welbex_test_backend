from rest_framework import viewsets
from rest_framework.mixins import RetrieveModelMixin, UpdateModelMixin
from rest_framework.viewsets import GenericViewSet

from delivery.models import Cargo, DeliveryCar
from delivery.serializers import DeliveryCarUpdateSerializer, CargoSerializer, CargoUpdateSerializer, \
    CargoCreateSerializer


class DeliveryCarUpdateAPIView(RetrieveModelMixin, UpdateModelMixin, GenericViewSet):
    queryset = DeliveryCar.objects.all()
    serializer_class = DeliveryCarUpdateSerializer


class CargoAPIView(viewsets.ModelViewSet):
    queryset = Cargo.objects.all()

    def get_serializer_class(self):
        if self.action in ['update', 'partial-update']:
            serializer_class = CargoUpdateSerializer
        elif self.action == 'create':
            serializer_class = CargoCreateSerializer
        else:
            serializer_class = CargoSerializer
        return serializer_class
