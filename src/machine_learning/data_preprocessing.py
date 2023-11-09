import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from config.log_config import logger


def load_data(filepath):
    try:
        data = pd.read_csv(filepath, sep=',')
        logger.info(f"Data loaded successfully from {filepath}")
        return data
    except Exception as e:
        logger.error(f"Error loading data from {filepath}: {e}")
        raise

def preprocess_data(data):
    try:
        X = data[['sensor_1', 'sensor_2']].values
        if 'label' in data.columns:
            y = data[['label']].values
            logger.info("Label column found and processed.")
        else:
            y = None
            logger.warning("Label column not found. Proceeding without labels.")
        X = StandardScaler().fit_transform(X)
        logger.info("Data preprocessing complete.")
        return X, y
    except Exception as e:
        logger.error(f"Error in data preprocessing: {e}")
        raise

def split_data(X, y, test_size=0.3, random_state=99):
    try:
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)
        logger.info("Data split into train and test sets.")
        return X_train, X_test, y_train, y_test
    except Exception as e:
        logger.error(f"Error in splitting data: {e}")
        raise
