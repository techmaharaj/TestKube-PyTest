# weather_service.py

import requests
from flask import Flask, request, jsonify
import pytest, os

app = Flask(__name__)

def get_weather(city_name):
    api_key = os.getenv('OPENWEATHER_API_KEY')
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200:
        weather_description = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        return {"city": city_name, "weather": weather_description, "temperature": temperature}
    else:
        return {"error": "City not found"}

@app.route('/weather', methods=['GET'])
def weather():
    city_name = request.args.get('city')
    if city_name:
        weather_data = get_weather(city_name)
        return jsonify(weather_data)
    else:
        return jsonify({"error": "Please provide a city name"})

# Tests
def test_get_weather_by_valid_city():
    city_name = "London"
    response = get_weather(city_name)
    assert response["city"] == city_name
    assert "weather" in response
    assert "temperature" in response

if __name__ == '__main__':
    app.run(debug=True)
