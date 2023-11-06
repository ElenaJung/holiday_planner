from .external_api import fetch_from_api
from .data_structures import map_daily_weather_to_location
from .utils import extract_lat_long, calculate_dates_within_forecast_range


def get_weather_data(original_start_date, original_end_date, locations):
    # TODO: check that start date is before end date and check if all are valid inputs
    latitudes, longitudes = extract_lat_long(locations)

    is_estimate = False
    start_date, end_date = calculate_dates_within_forecast_range(
        original_start_date, original_end_date
    )
    if start_date != original_start_date or end_date != original_end_date:
        is_estimate = True

    weather_data = fetch_from_api(latitudes, longitudes, start_date, end_date)

    weather_by_location = map_daily_weather_to_location(
        weather_data.json(), is_estimate
    )

    return weather_by_location
