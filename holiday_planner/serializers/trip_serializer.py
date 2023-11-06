from rest_framework import serializers
import logging
from ..models import Trip, Location
from .location_serializer import LocationSerializer

logger = logging.getLogger(__name__)


class TripSerializer(serializers.ModelSerializer):
    locations = LocationSerializer(many=True)

    class Meta:
        model = Trip
        fields = ["id", "owner_id", "name", "locations"]

    def create(self, validated_data):
        added_locations = validated_data.pop("locations", [])

        trip = Trip.objects.create(**validated_data)

        for location in added_locations:
            Location.objects.create(trip=trip, **location)

        return trip

    def update(self, instance, validated_data):  # FIXME: THIS DOES NOT WORK!
        added_locations = validated_data.pop("locations", [])
        instance.id = instance.id
        instance.name = validated_data.get("name", instance.name)
        instance.owner_id = validated_data.get("owner_id", instance.owner_id)

        for location in added_locations:
            location_id = location.get("id")
            try:
                location_object = Location.objects.get(id=location_id)
            except Location.DoesNotExist:
                location_object = Location(**location)
                location_object.save()

            location_object.location = location.get(
                "location", location_object.location
            )
            location_object.start_date = location.get(
                "start_date", location_object.start_date
            )
            location_object.end_date = location.get(
                "end_date", location_object.end_date
            )
            location_object.trip = instance
            location_object.save()
        instance.save()
