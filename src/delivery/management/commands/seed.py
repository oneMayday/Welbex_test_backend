from csv import reader
from decimal import Decimal
from itertools import islice
from random import choice, randint

from django.core.management import BaseCommand

from delivery.models import Location, DeliveryCar
from src.settings import BASE_DIR


# 'Seed' mode for clearing and seeding data
# 'Clear' mode only for clearing
MODE_REFRESH = 'seed'
MODE_CLEAR = 'clear'
SEEDING_FILE_NAME = 'uszips_fortest.csv'


class Command(BaseCommand):
    help = "Seed database"

    def add_arguments(self, parser):
        parser.add_argument('--mode', type=str, help="Mode")

    def handle(self, *args, **options):
        if options['mode'] == 'seed':
            message = 'Seeding'
        else:
            message = 'Clearing'

        self.stdout.write(f'{message} database...')
        run_seed(self, options['mode'])
        self.stdout.write(f'{message} is done!')


def create_locations():
    """ Create database records (Location) from csv-file: """
    temp_locations_list = []
    with open(f'{BASE_DIR}/{SEEDING_FILE_NAME}', encoding='utf-8') as seed_file:
        data = islice(reader(seed_file), 1, None)
        for row in data:
            temp_locations_list.append(
                Location(
                    city=row[5],
                    state=row[3],
                    zip=row[0],
                    latitude=Decimal(row[1]),
                    longitude=Decimal(row[2]),
                )
            )
        Location.objects.bulk_create(temp_locations_list, batch_size=999)


def create_delivery_machines(number_of_machines: int = 10):
    """ Create database records (DeliveryCar) """
    possible_ids = get_possible_ids()

    for i in range(number_of_machines):
        new_car = DeliveryCar(
                current_location=Location.objects.get(pk=choice(possible_ids)),
                tonnage=randint(1000, 10001)
            )
        new_car.save()


def run_seed(self, mode):
    """ Run seeding database """
    clear_data()
    if mode == MODE_CLEAR:
        return
    create_locations()
    create_delivery_machines()


def clear_data():
    """Delete all locations and cars from database"""
    DeliveryCar.objects.all().delete()
    Location.objects.all().delete()


def get_possible_ids():
    queryset = Location.objects.order_by('pk').all()
    possible_ids = list(queryset.values_list('id', flat=True))
    return possible_ids
