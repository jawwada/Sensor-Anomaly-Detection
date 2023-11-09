from flask import Flask, request, jsonify
from joblib import load
import pandas as pd

app = Flask(__name__)
model = load('models/model.joblib')  # Load the model

@app.route('/predict', methods=['POST'])
def predict():
    # Get data from POST request
    # Here you would convert the JSON data to the format your model expects
    data = pd.read_json(request.get_json())

    prediction = model.predict(data)
    return jsonify({'prediction': list(prediction)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)

