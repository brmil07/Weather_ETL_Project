from airflow import DAG
from datetime import timedelta, datetime
from airflow.providers.http.sensors.http import HttpSensor
import json
from airflow.providers.http.operators.http import SimpleHttpOperator
from airflow.operators.python import PythonOperator
import pandas as pd


def transform_load_data(task_instance):
    data = task_instance.xcom_pull(task_ids="extract_weather_data")
    city = data["name"]
    weather_description = data["weather"][0]['description']
    temp_metric = data["main"]["temp"]
    feels_like_metric= data["main"]["feels_like"]
    min_temp_metric = data["main"]["temp_min"]
    max_temp_metric = data["main"]["temp_max"]
    pressure = data["main"]["pressure"]
    humidity = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]
    time_of_record = datetime.utcfromtimestamp(data['dt'] + data['timezone'])
    sunrise_time = datetime.utcfromtimestamp(data['sys']['sunrise'] + data['timezone'])
    sunset_time = datetime.utcfromtimestamp(data['sys']['sunset'] + data['timezone'])

    transformed_data = {"City": city,
                        "Description": weather_description,
                        "Temperature (F)": temp_metric,
                        "Feels Like (F)": feels_like_metric,
                        "Minimun Temp (F)":min_temp_metric,
                        "Maximum Temp (F)": max_temp_metric,
                        "Pressure": pressure,
                        "Humidty": humidity,
                        "Wind Speed": wind_speed,
                        "Time of Record": time_of_record,
                        "Sunrise (Local Time)":sunrise_time,
                        "Sunset (Local Time)": sunset_time
                        }
    transformed_data_list = [transformed_data]
    df_data = pd.DataFrame(transformed_data_list)
    aws_credentials = {"key": "KEY",
                       "secret": "SECRET KEY",
                       "token": "TOKEN"}

    now = datetime.now()
    dt_string = now.strftime("%d%m%Y%H%M%S")
    dt_string = 'weather_data_berlin_' + dt_string
    df_data.to_csv(f"s3://my-weather-etl-project/{dt_string}.csv", index=False, storage_options=aws_credentials)


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 3, 12),
    'email': ['myemail@domain.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 2,
    'retry_delay': timedelta(minutes=2)
}


with DAG('weather_dag',
         default_args=default_args,
         schedule_interval = '@daily',
         catchup=False) as dag:


        is_weather_api_ready = HttpSensor(task_id ='is_weather_api_ready',
                                          http_conn_id='weathermap_api',
                                          endpoint='/data/2.5/weather?q=berlin&APPID=YOUR_API_KEY')

        extract_weather_data = SimpleHttpOperator(task_id='extract_weather_data',
                                                  http_conn_id='weathermap_api',
                                                  endpoint='/data/2.5/weather?q=berlin&APPID=YOUR_API_KEY',
                                                  method='GET',
                                                  response_filter=lambda r: json.loads(r.text),
                                                  log_response=True)

        transform_load_weather_data = PythonOperator(task_id='transform_load_weather_data',
                                                     python_callable=transform_load_data)

        is_weather_api_ready >> extract_weather_data >> transform_load_weather_data