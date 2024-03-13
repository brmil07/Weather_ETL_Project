# My Data Engineering Project
---
This is the repository for my personal ETL Project which is an End-to-End Data Engineering project to scrape weather data with weather API and Python. Performed Extract, Transform, and Load (ETL) operation where the data was first collected, transformed from JSON into CSV format, and the code was deployed on Airflow/EC2 and stored the final result in the Amazon S3.

Apache Airflow is an open-source platform used for orchestrating and scheduling workflows of tasks and data pipelines. It provides a way to programmatically manage, schedule, and monitor workflows. A Directed Acyclic Graph (DAG) in Apache Airflow is a collection of tasks with defined dependencies between them. Each task within the DAG represents a unit of work to be performed, and the dependencies define the order in which the tasks should be executed. The directed aspect of the graph indicates the flow of execution from one task to another, while acyclic ensures that there are no loops in the flow, preventing infinite execution cycles.

This project will use the following technologies:
- Python
- Weather API
- Airflow
- Amazon EC2
- Amazon S3

## Project execution:
1. Create an AWS account.
2. Create an EC2 instance, choose Ubuntu image, choose an instance type "t2.medium", create a key pair for login via SSH, and configure the security group to allow inbound traffic.
3. After all the configuration is done, launch the EC2 instance.
4. Connect to the EC2 instance via EC2 (via EC2 Instance Connect or SSH)

## References
* [Amazon Web Service](https://aws.amazon.com)
* [OpenWeatherMap API](https://openweathermap.org/api)
* [Twitter Data Pipeline using Airflow for Beginners | Data Engineering Project](https://youtu.be/q8q3OFFfY6c?si=GW8joWF8WDc0vRY-)
* [twitter-airflow-data-engineering-project](https://github.com/darshilparmar/twitter-airflow-data-engineering-project)
* [How to build and automate a python ETL pipeline with airflow on AWS EC2](https://youtu.be/uhQ54Dgp6To?si=lagZrfgKqbNbrTrJ)
* [data_engineering_project_openweathermap_api_airflow_etl_aws](https://github.com/YemiOla/data_engineering_project_openweathermap_api_airflow_etl_aws)
