# sensor_fault_detection/tests/test_model_training.py
import pytest
from sklearn.datasets import make_classification
from src.machine_learning.model import train_model

def test_train_model():
    # Create a synthetic dataset
    X, y = make_classification(n_samples=1000, n_features=2, n_informative=2, n_repeated=0, n_redundant=0, random_state=42)

    # Train the model
    model = train_model(X, y)

    # Assert the model is trained (e.g., by checking if model coefficients are set)
    assert hasattr(model, 'kernel_')
