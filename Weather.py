import openmeteo_requests

import requests_cache
import pandas as pd
from retry_requests import retry

import geopy
from geopy.geocoders import Nominatim

from json import loads, dumps

def getWeather(location, date):
    # Setup the Open-Meteo API client with cache and retry on error
    cache_session = requests_cache.CachedSession('.cache', expire_after = -1)
    retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
    openmeteo = openmeteo_requests.Client(session = retry_session)

    coordinates = longlanCity(location)
    # Make sure all required weather variables are listed here
    # The order of variables in hourly or daily is important to assign them correctly below
    url = "https://archive-api.open-meteo.com/v1/archive"
    params = {
        "latitude": coordinates[0],
        "longitude": coordinates[1],
        "start_date": date, # Format YYYY-MM-DD String
        "end_date": date,
        "daily": ["weather_code", "temperature_2m_max", "temperature_2m_min", "temperature_2m_mean", "daylight_duration", "precipitation_sum", "rain_sum", "snowfall_sum", "precipitation_hours", "wind_speed_10m_max", "wind_gusts_10m_max", "wind_direction_10m_dominant"]
    }
    responses = openmeteo.weather_api(url, params=params)

    # Process first location. Add a for-loop for multiple locations or weather models
    response = responses[0]
    #print(f"Coordinates {response.Latitude()}°N {response.Longitude()}°E")
    #print(f"Elevation {response.Elevation()} m asl")
    #print(f"Timezone {response.Timezone()} {response.TimezoneAbbreviation()}")
    #print(f"Timezone difference to GMT+0 {response.UtcOffsetSeconds()} s")

    # Process daily data. The order of variables needs to be the same as requested.
    daily = response.Daily()
    daily_weather_code = daily.Variables(0).ValuesAsNumpy()
    daily_temperature_2m_max = daily.Variables(1).ValuesAsNumpy()
    daily_temperature_2m_min = daily.Variables(2).ValuesAsNumpy()
    daily_temperature_2m_mean = daily.Variables(3).ValuesAsNumpy()
    daily_daylight_duration = daily.Variables(4).ValuesAsNumpy()
    daily_precipitation_sum = daily.Variables(5).ValuesAsNumpy()
    daily_rain_sum = daily.Variables(6).ValuesAsNumpy()
    daily_snowfall_sum = daily.Variables(7).ValuesAsNumpy()
    daily_precipitation_hours = daily.Variables(8).ValuesAsNumpy()
    daily_wind_speed_10m_max = daily.Variables(9).ValuesAsNumpy()
    daily_wind_gusts_10m_max = daily.Variables(10).ValuesAsNumpy()
    daily_wind_direction_10m_dominant = daily.Variables(11).ValuesAsNumpy()

    daily_data = {"date": date
        #pd.date_range(
        #start = pd.to_datetime(daily.Time(), unit = "s", utc = True),
        #end = pd.to_datetime(daily.TimeEnd(), unit = "s", utc = True),
        #freq = pd.Timedelta(seconds = daily.Interval()),
        #inclusive = "left"
        #)
    }
    daily_data["weather_code"] = daily_weather_code.tolist()
    daily_data["temperature_2m_max"] = daily_temperature_2m_max.tolist()
    daily_data["temperature_2m_min"] = daily_temperature_2m_min.tolist()
    daily_data["temperature_2m_mean"] = daily_temperature_2m_mean.tolist()
    daily_data["daylight_duration"] = daily_daylight_duration.tolist()
    daily_data["precipitation_sum"] = daily_precipitation_sum.tolist()
    daily_data["rain_sum"] = daily_rain_sum.tolist()
    daily_data["snowfall_sum"] = daily_snowfall_sum.tolist()
    daily_data["precipitation_hours"] = daily_precipitation_hours.tolist()
    daily_data["wind_speed_10m_max"] = daily_wind_speed_10m_max.tolist()
    daily_data["wind_gusts_10m_max"] = daily_wind_gusts_10m_max.tolist()
    daily_data["wind_direction_10m_dominant"] = daily_wind_direction_10m_dominant.tolist()

    
    #print(daily_data)

    #daily_dataframe = pd.DataFrame(data = daily_data)
    #print(daily_dataframe)

    return daily_data



def longlanCountry(city, country):
    geolocator = Nominatim()
    loc = geolocator.geocode(city+','+ country)
    return (loc.latitude, loc.longitude)

def longlanCity(city):
    geolocator = Nominatim(user_agent="Your_Name")
    location = geolocator.geocode(city)
    return (location.latitude, location.longitude)

getWeather("London", "2022-09-21")