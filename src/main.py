from src.machine_learning.data_preprocessing import load_data, preprocess_data, split_data
from src.machine_learning.model import train_model, evaluate_model
from src.machine_learning.inference import predict, add_predictions_to_dataframe
from joblib import dump

def main():
    # Load and preprocess data
    data = load_data("data/historical_sensor_data.csv")
    X, y = preprocess_data(data)
    X_train, X_test, y_train, y_test = split_data(X, y)

    # Train model
    clf = train_model(X_train, y_train)

    # Evaluate model
    score = evaluate_model(clf, X_test, y_test)
    print(f"Model score: {score}")

    # Assuming your model is named 'model'
    dump(clf, 'models/model.joblib')

    # Inference
    latest_data = load_data("data/latest_sensor_data.csv")
    X_latest = preprocess_data(latest_data)[0]
    predictions = predict(clf, X_latest)
    results = add_predictions_to_dataframe(latest_data, predictions)
    print(results.head())

if __name__ == "__main__":
    main()
