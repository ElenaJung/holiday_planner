from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema
from ..models import Location, Trip
from ..serializers import LocationSerializer, TripSerializer


@extend_schema(request=TripSerializer, responses={200: TripSerializer})
@api_view(["GET", "PUT", "DELETE"])
def trip_id(request, id):
    try:
        trip = Trip.objects.get(pk=id)
    except Trip.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = TripSerializer(trip)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = TripSerializer(trip, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        trip.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
