sudo apt-get update -y
sudo apt-get upgrade -y
sudo apt install python3-pip -y
sudo apt install python3.10-venv

python3 -m venv airflow_venv
pip install pandas
pip install s3fs
pip install apache-airflow
pip install apache-airflow[cncf.kubernetes]

sudo apt install awscli
aws configure
aws sts get-session-token

airflow standalone