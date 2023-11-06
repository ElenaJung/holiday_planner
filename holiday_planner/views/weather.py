from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema, OpenApiParameter
from typing import List

from ..fetch_data.weather.get_weather_data import get_weather_data


@extend_schema(
    parameters=[
        OpenApiParameter(
            name="start_date",
            description="start date of trip",
            type=str,
            default="2023-11-08",
        ),
        OpenApiParameter(
            name="end_date",
            description="end date of trip",
            type=str,
            default="2023-11-15",
        ),
        OpenApiParameter(
            name="locations",
            description="lat,long of locations",
            type=str,  # TODO: should be array not str
            default="52.52437,13.41053+35.6895,139.69171+48.13743,11.57549",
        ),
    ]
)
@api_view(["GET"])
def weather(request):
    start_date = request.query_params.get("start_date")
    end_date = request.query_params.get("end_date")
    locations = request.query_params.get("locations")

    weather_data = get_weather_data(start_date, end_date, locations)

    return Response(weather_data, status=status.HTTP_200_OK)
