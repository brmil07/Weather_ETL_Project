import pytest
import requests
from local.weather import get_weather, print_weather
from unittest.mock import patch
from local.secrets import API_KEY
from local.config import BASE_URL

# Test the get_weather function
def test_get_weather_success():
    city_name = "London"
    expected_response = {
        "name": "London",
        "main": {
            "temp": 15,
            "humidity": 75,
            "pressure": 1012
        },
        "weather": [
            {"description": "clear sky"}
        ],
        "wind": {
            "speed": 5.1
        }
    }
    
    # Mock the requests.get method to return a response with the expected JSON data
    with patch('requests.get') as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = expected_response

        response = get_weather(city_name)
        assert response == expected_response

def test_get_weather_failure():
    city_name = "InvalidCity"
    
    # Mock the requests.get method to return a 404 response
    with patch('requests.get') as mock_get:
        mock_get.return_value.status_code = 404

        response = get_weather(city_name)
        assert response is None

# Test the print_weather function
def test_print_weather_success(capsys):
    data = {
        "name": "London",
        "main": {
            "temp": 15,
            "humidity": 75,
            "pressure": 1012
        },
        "weather": [
            {"description": "clear sky"}
        ],
        "wind": {
            "speed": 5.1
        }
    }
    
    print_weather(data)
    
    captured = capsys.readouterr()
    assert "City: London" in captured.out
    assert "Temperature: 15°C" in captured.out
    assert "Humidity: 75%" in captured.out
    assert "Pressure: 1012 hPa" in captured.out
    assert "Weather: Clear sky" in captured.out
    assert "Wind Speed: 5.1 m/s" in captured.out

def test_print_weather_failure(capsys):
    print_weather(None)
    
    captured = capsys.readouterr()
    assert "Error: City not found or API limit exceeded." in captured.out