import openmeteo_requests
import pandas as pd
from retry_requests import retry
from django.core.cache import cache
import requests  # Import requests for the session

# Setup the Open-Meteo API client with retry on error
retry_session = retry(requests.Session(), retries=5, backoff_factor=0.2)  # Fixed requests import
openmeteo = openmeteo_requests.Client(session=retry_session)


def get_daily_weather_data(latitude, longitude):
    # Cache key based on coordinates for daily weather data
    cache_key = f"daily_weather_data_{latitude}_{longitude}"

    # Try to get cached data
    response = cache.get(cache_key)
    if response is None:
        # If cache is empty, make the API request for daily data
        url = "https://api.open-meteo.com/v1/forecast"
        params = {
            "latitude": latitude,
            "longitude": longitude,
            "daily": "temperature_2m_max,temperature_2m_min",
            "timezone": "auto"
        }

        # Fetch the weather data using Open-Meteo API
        responses = openmeteo.weather_api(url, params=params)
        response = responses[0]

        # Cache the response for 1 hour (3600 seconds)
        cache.set(cache_key, response, timeout=3600)

    # Process the response data
    print(f"Coordinates {response.Latitude()}°N {response.Longitude()}°E")
    print(f"Elevation {response.Elevation()} m asl")
    print(f"Timezone {response.Timezone()} {response.TimezoneAbbreviation()}")
    print(f"Timezone difference to GMT+0 {response.UtcOffsetSeconds()} s")

    # Process daily data
    daily = response.Daily()
    daily_temperature_max = daily.Variables(0).ValuesAsNumpy()
    daily_temperature_min = daily.Variables(1).ValuesAsNumpy()

    # Create pandas DataFrame for daily data
    daily_data = {
        "date": pd.date_range(
            start=pd.to_datetime(daily.Time(), unit="s", utc=True),
            end=pd.to_datetime(daily.TimeEnd(), unit="s", utc=True),
            freq=pd.Timedelta(days=1),
            inclusive="left"
        ),
        "temperature_max": daily_temperature_max,
        "temperature_min": daily_temperature_min
    }

    daily_dataframe = pd.DataFrame(data=daily_data)

    return daily_dataframe
