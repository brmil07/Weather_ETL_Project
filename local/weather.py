import requests
import sys
from datetime import datetime
from local.config import BASE_URL
from local.secrets import API_KEY

def get_weather(city_name):
    """
    Fetch the weather data for a given city using the OpenWeatherMap API.
    
    :param city_name: Name of the city to fetch the weather for.
    :return: JSON response from the API containing weather data.
    """
    # Construct the URL for historical data for the current date
    current_date = datetime.today()
    unix_timestamp = int(current_date.timestamp())
    url = BASE_URL + "appid=" + API_KEY + "&q=" + city_name + "&units=metric" + "&dt=" + str(unix_timestamp)

    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        return None

def print_weather(data):
    """
    Print the weather data in a readable format.
    
    :param data: JSON response containing weather data.
    """
    if data:
        main = data['main']
        wind = data['wind']
        weather = data['weather'][0]
        
        print(f"City: {data['name']}")
        print(f"Temperature: {main['temp']}°C")
        print(f"Humidity: {main['humidity']}%")
        print(f"Pressure: {main['pressure']} hPa")
        print(f"Weather: {weather['description'].capitalize()}")
        print(f"Wind Speed: {wind['speed']} m/s")
    else:
        print("Error: City not found or API limit exceeded.")

def main():
    if len(sys.argv) != 2:
        print("Usage: python weather.py <city_name>")
        sys.exit(1)
    
    city_name = sys.argv[1]
    data = get_weather(city_name)
    print_weather(data)

if __name__ == "__main__":
    main()