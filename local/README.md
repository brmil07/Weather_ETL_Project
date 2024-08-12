***
# Weather API Project
***
This project is a simple command-line tool that fetches the current weather for a given city using the OpenWeatherMap API.

## Prerequisites

- Python 3.8+
- An API key from: [OpenWeatherMap](https://openweathermap.org/api)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/brmil07/Weather_ETL_Project.git
    ```

2. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

3. Add your API key to the `secrets.py` file.

## Usage

Example on how to run the script:

```bash
python weather.py <city_name>
```

***
# How to run the script using Docker
***
- Navigate to the directory containing the Dockerfile and run the following command to build the Docker image
- Build the docker image:
```basg
docker build -t weather-api .
```
- After building the image, run the container with the following command:
```bash
docker run --rm weather-api python weather.py <city_name>
```