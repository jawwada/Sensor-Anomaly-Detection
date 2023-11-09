# sensor_fault_detection/tests/test_data_preprocessing.py
import pytest
import pandas as pd
from src.machine_learning.data_preprocessing import preprocess_data

def test_extract_label():
    # Create a sample DataFrame with a 'label' column
    data = pd.DataFrame({
        'sensor_1': [0.5, -0.1, 0.3],
        'sensor_2': [1.2, -0.7, 0.8],
        'label': [0, 1, 0]
    })

    # Assuming preprocess_data returns a tuple (X, y)
    _, y = preprocess_data(data)

    # Expected output
    expected_y = data[['label']].values

    # Check if the extracted labels match the expected labels
    assert (y == expected_y).all(), "Labels do not match the expected values"

    # Optionally, also check the shape
    assert y.shape == (len(data), 1), "Shape of the labels is incorrect"
