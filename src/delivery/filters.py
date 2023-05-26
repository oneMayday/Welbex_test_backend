from django_filters import rest_framework as filters

from delivery.models import Cargo


class WeightFilter(filters.FilterSet):
    min_weight = filters.NumberFilter(field_name='weight', lookup_expr='gte')
    max_weight = filters.NumberFilter(field_name='weight', lookup_expr='lte')

    class Meta:
        model = Cargo
        fields = ['weight']
