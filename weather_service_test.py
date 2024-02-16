# test_weather_service.py
import pytest
import requests
from weather_service import get_weather

def test_get_weather_by_valid_city():
    city_name = "London"
    response = get_weather(city_name)
    assert response["city"] == city_name
    assert "weather" in response
    assert "temperature" in response


