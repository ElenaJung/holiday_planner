import requests


def fetch_from_api(latitudes, longitudes, start_date, end_date):
    weather_base_url = "https://api.open-meteo.com/v1/forecast"
    locations = f"latitude={latitudes}&longitude={longitudes}"
    time_range = f"start_date={start_date}&end_date={end_date}"
    query_options = "daily=temperature_2m_max,temperature_2m_min"

    weather_url = f"{weather_base_url}?{locations}&{time_range}&{query_options}"

    response = requests.get(weather_url)

    return response
