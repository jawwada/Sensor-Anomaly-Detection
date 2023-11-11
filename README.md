# Sensor Fault Detection

## Project Overview
This project focuses on fault detection in sensor data, leveraging a Python-based machine learning model for analysis and inference. Additionally, it showcases model deployment via a Docker-based Flask web server, enabling request handling and server interaction. 
Key features and processes within the project include:

1. **Data Preprocessing:** Implementation of data cleaning and preparation for analysis.
2. **Model Training:** Development of machine learning algorithms for pattern recognition.
3. **Model Inference:** Application of the trained model to new data for fault detection.
4. **Model Deployment:** Deployment of the model using a Docker container and Flask web server.
5. **CI/CD Pipeline:** Integration of Continuous Integration and Continuous Deployment using Azure DevOps, including automated push to Azure Container Registry.
6. **Unit Testing:** Ensuring code quality and functionality with Pytest.
7. **Logging:** Utilization of the Python Logging Module for efficient tracking and debugging.
8. **API Interaction:** Demonstration of sending requests to the Flask server and receiving responses.


## Requirements
- Python 3.8
- Docker (for Docker-based setup)
- PyCharm or Visual Studio Code (for IDE-based setup)

## Quick Start

To run the project from shell/locally , navigate to the project directory set the PYTHONPATH:
```bash
cd sensor_fault_detection
export PYTHONPATH="${PYTHONPATH}:$(pwd)"
```
There is a data folder in the project root: sensor_fault_detection directory
1. add data files historical_sensor_data.csb and latest_sensor_data.csv to data folder
2. add model.ipynb to notebooks folder


Install the required packages:

```bash
pip install -r requirements.txt
```

## Alternative Setups
### 1. Local Setup

Running the main script:
```bash
python src/main.py
```
Running the tests:
```bash
pytest
```
Running the Flask server:
```bash
python src/app/app.py
```
Keep server running, open another prompt, go to project root, setup python path like above and make example request for model inference:
```bash
python src/app/request.py
```

### 2. Docker Setup
To build and run the project using Docker:
```bash
docker build -t sensor_fault_detection .
docker run -p 80:80 sensor_fault_detection
```
Keep server running, open another prompt, go to project root, setup python path like above and make example request for model inference:
```bash
python src/app/request.py
```
### 3. IDE Setup
To run the project using an IDE, first set the working directory to project root
then run any of the files in the `src` directory.
1. to run the main script, set the working directory to project root and run `main.py` in the `src` directory.
2. run app.py in the app directory to start the flask server.
3. run request.py in the request directory to make a request to the flask server.

## CI/CD Pipeline
The CI/CD pipeline is implemented using Azure DevOps. The pipeline is triggered when a new tag is pushed to the repository. The pipeline builds the Docker image and pushes it to the Azure Container Registry. The pipeline is defined in the `sensor_fault_detection.yaml` file.
process given below:
1. Create a new tag in gitlab
2. Pipeline will be triggered and build the docker image
3. Push the docker image to azure container registry
4. Kubernetes or app service will be deployed with the latest image



## Project Structure
The project is structured as follows:
```bash
sensor_fault_detection
├── config
│   ├── log_config.py
├── data
│   ├── historical_sensor_data.csb
│   ├── latest_sensor_data.csv
├── models
│   ├── model.joblib
├── notebooks
│   ├── model.ipynb
├── src
│   ├── app
│   │   ├── app.py
│   ├── request
│   │   ├── request.py
│   ├── init.py       
│   ├── main.py
│   ├── machine_learning
│   │   ├── inference.py
│   │   ├── model.py
│   │   ├── data_preprocessing.py
├── tests
│   ├── test_data_preprocessing.py
│   ├── test_model_training.py
├── Dockerfile
├── README.md
├── requirements.txt
├── .gitignore
├── sensor_fault_detection.yaml
```
## Project Components

The project consists of the following components:
- **config**: Contains the configuration files for the project. Logging, Database, Blob Storage, etc.
- **data**: Contains the historical and latest sensor data.
- **models**: Contains the trained model.
- **notebooks**: Contains the Jupyter notebook used for model training.
- **src**: Contains the source code for the project.
  - **app**: Contains the Flask web server for handling requests.
  - **request**: Contains the script for making requests to the Flask server.
  - **init.py**: Contains the initialization code for the project.
  - **main.py**: Contains the main script for the project.
  - **machine_learning**: Contains the machine learning code for the project.
    - **inference.py**: Contains the code for making inferences using the trained model.
    - **model.py**: Contains the code for training the model.
    - **data_preprocessing.py**: Contains the code for preprocessing the data.
- **tests**: Contains the unit tests for the project.
- **Dockerfile**: Contains the Dockerfile for the project.
- **README.md**: Contains the project overview and setup instructions.
- **requirements.txt**: Contains the required packages for the project.
- **sensor_fault_detection.yaml**: Contains CI/CD pipeline to push the container image to azure container registry through azure devops/ gitlab tag push.

The project has logging for the main model building and inference tasks implemented using the Python logging module. The logs are stored in the `logs` directory which is created once the main script is run.
TODO: Add logging to the Flask server. Can be done using the Flask logging module.
TODO: Add logging to the unit tests. Can be done using the pytest logging module.

