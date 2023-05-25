import random
import string

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Location(models.Model):
	city = models.CharField(max_length=30)
	state = models.CharField(max_length=30)
	zip = models.CharField()
	latitude = models.DecimalField(max_digits=8, decimal_places=5, validators=[MinValueValidator(-90), MaxValueValidator(90)])
	longitude = models.DecimalField(max_digits=8, decimal_places=5, validators=[MinValueValidator(-180), MaxValueValidator(180)])


class Cargo(models.Model):
	pickup_location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, related_name='pickup')
	delivery_location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, related_name='delivery')
	weight = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(1000)])
	description = models.TextField(max_length=1000)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)


class DeliveryCar(models.Model):
	car_id = models.CharField(editable=False, unique=True)
	current_location = models.ForeignKey(
		Location,
		on_delete=models.SET_NULL,
		null=True,
		related_name='current_position'
	)
	tonnage = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(1000)])
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)
		if not self.car_id:
			allowed_letters = string.ascii_uppercase
			self.car_id = str(random.randrange(1000, 10000)) + random.choice(allowed_letters)
			self.save()
