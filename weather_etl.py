from datetime import datetime
import requests
import pandas as pd

def run_etl():
    BASE_URL = 'http://api.openweathermap.org/data/2.5/weather?'
    API_KEY = 'c398a640e680959730b54b96d6876dda'

    CITY_LIST = ['berlin', 'cologne', 'duisburg', 'essen', 'hamburg', 'frankfurt', 'munich', 'stuttgart']
    response_data = []

    current_date = datetime.today()
    unix_timestamp = int(current_date.timestamp())

    for i in range(len(CITY_LIST)):
        CITY = CITY_LIST[i]
        # Construct the URL for historical data for the current date
        url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY + "&units=metric" + "&dt=" + str(unix_timestamp)

        # Make the request and append the response to the list
        response = requests.get(url).json()
        response_data.append(response)

    # Convert the nested JSON data into a pandas DataFrame
    df = pd.json_normalize(response_data[0])
    data_df = pd.concat([df.drop(columns=['weather']), pd.json_normalize(df['weather'][0])], axis=1)
    
    df = pd.DataFrame(response_data)
    df.to_csv('weather_german_cities.csv')