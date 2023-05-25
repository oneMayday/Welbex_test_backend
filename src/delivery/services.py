from decimal import Decimal

from geopy.distance import geodesic

from delivery.models import Location


def get_distance_in_miles_between_cities(city1: Location, city2: Location) -> Decimal:
    city1_coordinates = (city1.latitude, city1.longitude)
    city2_coordinates = (city2.latitude, city2.longitude)
    distance = Decimal(geodesic(city1_coordinates, city2_coordinates).miles)
    return distance
