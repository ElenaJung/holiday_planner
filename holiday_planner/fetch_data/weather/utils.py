from datetime import datetime, timedelta


def extract_lat_long(locations):
    # 52.52437,13.41053+35.6895,139.69171+48.13743,11.57549
    latlongs = locations.split("+")
    latitudes = [latlong.split(",")[0] for latlong in latlongs]
    longitudes = [latlong.split(",")[1] for latlong in latlongs]

    return ",".join(latitudes), ",".join(longitudes)


def calculate_dates_within_forecast_range(start_date, end_date):
    start_date = datetime.strptime(start_date, "%Y-%m-%d")
    end_date = datetime.strptime(end_date, "%Y-%m-%d")
    date_in_two_weeks = datetime.now() + timedelta(days=14)

    if start_date > date_in_two_weeks or end_date > date_in_two_weeks:
        one_year_in_days = 365
        start_date = start_date - timedelta(one_year_in_days)
        end_date = end_date - timedelta(one_year_in_days)

    return start_date.strftime("%Y-%m-%d"), end_date.strftime("%Y-%m-%d")
