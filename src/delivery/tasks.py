from random import choice

from celery import shared_task

from delivery.models import DeliveryCar, Location
from delivery.services import get_possible_locations


@shared_task(name='update_delivery_cars_locations')
def update_delivery_cars_locations():
	delivery_cars = DeliveryCar.objects.all()
	possible_locations = get_possible_locations()

	for car in delivery_cars:
		new_current_location = Location.objects.get(pk=choice(possible_locations))
		car.current_location = new_current_location
		car.save()
