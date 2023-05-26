from rest_framework import serializers

from delivery.models import Location, Cargo, DeliveryCar
from delivery.services import get_cars_nearby, get_all_distances


# Location model serializers
class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'
        read_only_fields = ('__all__',)


class LocationSimpledSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('zip', 'city', 'state',)
        read_only_fields = ('city', 'state',)


# DeliveryCar model serializers
class DeliveryCarsCargoDetailSerializer(serializers.ModelSerializer):
    distance = serializers.IntegerField()

    class Meta:
        model = DeliveryCar
        fields = ('pk', 'car_id', 'distance',)



class DeliveryCarUpdateSerializer(serializers.ModelSerializer):
    current_location = LocationSimpledSerializer(many=False)

    class Meta:
        model = DeliveryCar
        fields = ('pk', 'car_id', 'current_location',)

    def update(self, instance, validated_data):
        new_location = validated_data.get('current_location', instance.current_location)
        new_location_zip = new_location.get('zip')

        try:
            new_location = Location.objects.get(zip=new_location_zip)
        except Exception:
            msg = 'Wrong zip code'
            raise Exception(msg)

        instance.current_location = new_location
        instance.save()
        return instance


# Cargo model serializers
class CargoDetailSerializer(serializers.ModelSerializer):
    pickup = LocationSimpledSerializer(many=False)
    delivery = LocationSimpledSerializer(many=False)
    allowed_cars = serializers.SerializerMethodField()

    class Meta:
        model = Cargo
        fields = ('pk', 'weight', 'description', 'pickup', 'delivery', 'allowed_cars',)

    def get_allowed_cars(self, instance):
        """ Get all deliverycars with distances to cargo"""
        cars_nearby = get_all_distances(instance)
        serialized_data = DeliveryCarsCargoDetailSerializer(cars_nearby, many=True)
        return serialized_data.data


class CargoListSerializer(serializers.ModelSerializer):
    pickup = LocationSimpledSerializer(many=False)
    delivery = LocationSimpledSerializer(many=False)
    cars_nearby = serializers.SerializerMethodField()

    class Meta:
        model = Cargo
        fields = ('pk', 'pickup', 'delivery', 'cars_nearby',)

    def get_cars_nearby(self, instance):
        quantity_cars_nearby = len(get_cars_nearby(instance))
        return quantity_cars_nearby


class CargoCreateSerializer(serializers.ModelSerializer):
    pickup = LocationSimpledSerializer(many=False)
    delivery = LocationSimpledSerializer(many=False)

    class Meta:
        model = Cargo
        fields = ('weight', 'description', 'pickup', 'delivery', )

    def create(self, validated_data):
        weight = validated_data.get('weight')
        description = validated_data.get('description')
        location_pickup_zip = validated_data.get('pickup').get('zip')
        location_delivery_zip = validated_data.get('delivery').get('zip')

        try:
            location_pickup = Location.objects.get(zip=location_pickup_zip)
            location_delivery = Location.objects.get(zip=location_delivery_zip)
        except Exception:
            msg = 'Wrong zip codes'
            raise Exception(msg)

        try:
            instance = Cargo.objects.create(
                pickup=location_pickup,
                delivery=location_delivery,
                weight=weight,
                description=description
            )
            return instance
        except TypeError:
            msg = "Can't create new cargo instance"
            raise Exception(msg)


class CargoUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cargo
        fields = ('weight', 'description',)
