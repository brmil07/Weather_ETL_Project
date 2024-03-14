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
5. Run the following commands after the instance is ready
* Update and upgrade all packages to the latest version:
```bash
sudo apt install python3-pip -y
sudo apt install python3.10-venv
```
* Install Python:
```bash
sudo apt install python3-pip -y
sudo apt install python3.10-venv
```
* Create airflow environment:
```bash
python3 -m venv airflow_venv
```
* Install all the necessary libraries:
```bash
pip install pandas
pip install s3fs
pip install apache-airflow
pip install apache-airflow[cncf.kubernetes]
```
* Check if Airflow is working properly or not:
```bash
airflow
```
---
> NOTE: If the 'airflow' command is not found, please do the following steps:
* Edit the bashrc file
```bash
nano ~/.bashrc
```
* Add the following line into the .bashrc file:
```bash
export PATH="$PATH:/path/to/airflow/bin"
```
* Source the .bashrc file:
```bash
source ~/.bashrc
```
* Now we can check the following command
```bash
airflow
```
---
* Install the AWS CLI:
```bash
sudo apt install awscli
```
* Configure the AWS and input the access key and secret access key (We need to create an access key in our AWS account in my security credentials section):
```bash
aws configure
```
* We need to get the session token. We need to execute the following command (Please save the Access Key ID, Secret Access Key, and Session Token. Watch out for the expiration period):
```bash
aws sts get-session-token
```
* Run the Apache Airflow Server (the username and password will be after the server is running):
```bash
airflow standalone
```
6. Connect to the Airflow server through port 8080: ``HTTP://YOUR_PUBLIC_IPv4_ADRESS:8080``
7. Should it have a problem with the connection, please check again the policies in the security groups.
8. Press `CTRL + C` to shut down the Airflow server
9. Create an S3 bucket to store the data later
10. We need to modify the IAM role of our instance so it has access to the S3 bucket. For this project purpose, we can assign S3 and EC2 full access.
11. To specify the DAG file, we need to do some modifications:
* Navigate to the 'airflow' folder:
```bash
cd airflow
```
* Create a directory to place the DAG file:
```bash
mkdir weather_dag
```
* Check the directory contents:
```bash
ls
```
* Edit the configuration file with the preferred file editor:
```bash
sudo nano airflow.cfg
```
* Change the "dags_folder" path to: "home/ubuntu/airflow/weather_dag". Then close and save.
* We can put the python DAG file ``weather_dag.py`` into the "weather_dag" directory that has been created previously.
* Now the Airflow server can be executed:
```bash
airflow standalone
```
12. After the Airflow server is running, we need to add a connection to the API Host, navigate to the admin section, add a new connection, and fill in the form as follows:
![Airflow Add Connection Image](https://github.com/brmil07/Weather_ETL_Project/blob/main/add_connection_airflow.png)
13. If all of the configuration are done properly, we could execute the DAG task.
14. The end result will be a CSV file stored in our S3 bucket.

## References
* [Amazon Web Service](https://aws.amazon.com)
* [OpenWeatherMap API](https://openweathermap.org/api)
* [Twitter Data Pipeline using Airflow for Beginners | Data Engineering Project](https://youtu.be/q8q3OFFfY6c?si=GW8joWF8WDc0vRY-)
* [twitter-airflow-data-engineering-project](https://github.com/darshilparmar/twitter-airflow-data-engineering-project)
* [How to build and automate a python ETL pipeline with airflow on AWS EC2](https://youtu.be/uhQ54Dgp6To?si=lagZrfgKqbNbrTrJ)
* [data_engineering_project_openweathermap_api_airflow_etl_aws](https://github.com/YemiOla/data_engineering_project_openweathermap_api_airflow_etl_aws)
