from rest_framework import serializers
from ..models import Location


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ["id", "location", "start_date", "end_date"]
