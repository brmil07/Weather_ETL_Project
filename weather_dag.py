from datetime import timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from datetime import datetime
from weather_etl import run_etl

default_args = {
    'owner': 'airflow-bryan',
    'depends_on_past': False,
    'start_date': datetime(2024, 3, 8),
    'email': ['bryanmilleanno@yahoo.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}

dag = DAG(
    'cities_weather_dag',
    default_args=default_args,
    description='DAG with ETL process',
    schedule_interval=timedelta(days=1),
)

run_etl_process = PythonOperator(
    task_id='complete_weather_etl',
    python_callable=run_etl,
    dag=dag,
)

run_etl_process