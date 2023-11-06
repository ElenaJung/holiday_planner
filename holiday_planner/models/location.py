from django.db import models

from .trip import Trip


class Location(models.Model):
    location = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name="locations")

    class Meta:
        indexes = [models.Index(fields=["trip"])]

    def __str__(self):
        return f"{self.location} ({self.trip.name})"
