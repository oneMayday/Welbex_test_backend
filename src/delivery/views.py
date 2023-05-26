from django_filters import rest_framework as filters
from rest_framework import viewsets
from rest_framework.mixins import RetrieveModelMixin, UpdateModelMixin, ListModelMixin
from rest_framework.viewsets import GenericViewSet

from delivery.models import Cargo, DeliveryCar, Location
from delivery.serializers import (
    CargoUpdateSerializer,
    CargoCreateSerializer,
    CargoListSerializer,
    CargoDetailSerializer,
    DeliveryCarUpdateSerializer,
    LocationSerializer,
)
from delivery.filters import WeightFilter


class CargoAPIView(viewsets.ModelViewSet):
    queryset = Cargo.objects.all()
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = WeightFilter

    def get_serializer_class(self):
        if self.action in ['update', 'partial-update']:
            serializer_class = CargoUpdateSerializer
        elif self.action == 'create':
            serializer_class = CargoCreateSerializer
        elif self.action == 'list':
            serializer_class = CargoListSerializer
        else:
            serializer_class = CargoDetailSerializer
        return serializer_class


class DeliveryCarAPIView(ListModelMixin, RetrieveModelMixin, UpdateModelMixin, GenericViewSet):
    queryset = DeliveryCar.objects.all()
    serializer_class = DeliveryCarUpdateSerializer


class LocationAPIView(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
