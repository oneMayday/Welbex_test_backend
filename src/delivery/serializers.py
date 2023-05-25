from rest_framework import serializers

from delivery.models import Location, Cargo, DeliveryCar


class LocationSerializer(serializers.ModelSerializer):
    city = serializers.CharField(read_only=True)
    state = serializers.CharField(read_only=True)
    longitude = serializers.CharField(read_only=True)
    latitude = serializers.CharField(read_only=True)

    class Meta:
        model = Location
        fields = ('zip', 'city', 'state', 'longitude', 'latitude',)


class DeliveryCarUpdateSerializer(serializers.ModelSerializer):
    current_location = LocationSerializer(many=False)

    class Meta:
        model = DeliveryCar
        fields = ('car_id', 'current_location',)

    def update(self, instance, validated_data):
        new_location = validated_data.get('current_location', instance.current_location)
        new_location_zip = new_location.get('zip')

        new_location = Location.objects.get(zip=new_location_zip)
        instance.current_location = new_location
        instance.save()
        return instance


class CargoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cargo
        exclude = ('created_at', 'updated_at',)


# class CargoListSerializer(serializers.ModelSerializer):
#     pickup_location = LocationSerializer(many=False)
#     delivery_location = LocationSerializer(many=False)
#     cars_nearby =
#
#     class Meta:
#         model = Cargo
#         fields = ('pk', 'pickup_location', 'delivery_location', 'cars_nearby')


class CargoCreateSerializer(serializers.ModelSerializer):
    pickup_location = LocationSerializer(many=False)
    delivery_location = LocationSerializer(many=False)

    class Meta:
        model = Cargo
        fields = ('pk', 'weight', 'description', 'pickup_location', 'delivery_location', )

    def create(self, validated_data):
        weight = validated_data.get('weight')
        description = validated_data.get('description')
        location_pickup_zip = validated_data.get('pickup_location').get('zip')
        location_delivery_zip = validated_data.get('delivery_location').get('zip')

        location_pickup = Location.objects.get(zip=location_pickup_zip)
        location_delivery = Location.objects.get(zip=location_delivery_zip)

        try:
            instance = Cargo.objects.create(
                pickup_location=location_pickup,
                delivery_location=location_delivery,
                weight = weight,
                description = description
            )
            return instance
        except TypeError:
            msg = "Can't create new cargo instance"
            raise TypeError(msg)


class CargoUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cargo
        fields = ('weight', 'description',)
