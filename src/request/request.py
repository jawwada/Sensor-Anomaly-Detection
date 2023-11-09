import requests
import pandas as pd
from src.machine_learning.data_preprocessing import load_data
#give the url of the docker container running the flask app and the port number
url = 'http://127.0.0.1:80/predict'
# get data from csv file to convert to json
data = load_data("data/latest_sensor_data.csv").to_json()
headers = {
    'Content-Type': 'application/json'
}

# make POST request to server
response = requests.post(url, json=data, headers=headers)

# check status code for response received
if response.status_code == 200:
    predictions = response.json()['prediction']
    print(predictions)
else:
    print('Error calling Flask app:', response.status_code)