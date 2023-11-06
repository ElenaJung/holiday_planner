from typing import List


def map_daily_weather_to_location(weather, is_estimate):
    result = []
    if not isinstance(weather, List):
        weather = [weather]

    for data in weather:
        latitude = data["latitude"]
        longitude = data["longitude"]
        daily_data = data["daily"]
        dates = daily_data["time"]
        temp_max = daily_data["temperature_2m_max"]
        temp_min = daily_data["temperature_2m_min"]
        all_weather = []
        for daily_data in zip(dates, temp_max, temp_min):
            all_weather.append(
                {
                    "date": daily_data[0],
                    "max_temp": daily_data[1],
                    "min_temp": daily_data[2],
                    "is_estimate": is_estimate,
                }
            )
        weather_by_location = {
            "location": (latitude, longitude),
            "weather": all_weather,
        }
        result.append(weather_by_location)
    return result
