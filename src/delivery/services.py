from decimal import Decimal

from geopy.distance import geodesic

from delivery.models import Cargo, DeliveryCar, Location


def get_distance_between(coords1: tuple, coords2: tuple) -> Decimal:
    """ Return distance between coordinates. """
    distance = Decimal(geodesic(coords1, coords2).miles).quantize(Decimal('0'))
    return distance


def get_cars_nearby(instance: Cargo) -> list | list[DeliveryCar]:
    """ Return list of delivery cars near the cargo or empty list. """
    try:
        inst_coord = (instance.pickup.latitude, instance.pickup.longitude)
        all_deliverycars = DeliveryCar.objects.select_related('current_location').all()
        cars_nearby = []
        for car in all_deliverycars:
            car_coords = car.current_location.latitude, car.current_location.longitude
            if get_distance_between(inst_coord, car_coords) <= 450:
                cars_nearby.append(car)
    except AttributeError:
        return []
    return cars_nearby


def get_all_distances(instance: Cargo) -> list[DeliveryCar]:
    """ Return list of delivery cars complemented with distance to cargo or empty list. """
    try:
        inst_coord = (instance.pickup.latitude, instance.pickup.longitude)
        all_delivery_cars_with_distance_to_cargo = []
        for car in DeliveryCar.objects.select_related('current_location').all():
            car_coords = car.current_location.latitude, car.current_location.longitude
            distance = get_distance_between(inst_coord, car_coords)
            car.distance = distance
            all_delivery_cars_with_distance_to_cargo.append(car)
    except AttributeError:
        return []
    return all_delivery_cars_with_distance_to_cargo


def get_possible_locations():
    queryset = Location.objects.order_by('pk').all()
    possible_ids = list(queryset.values_list('id', flat=True))
    return possible_ids
