
import numpy as np
from config.log_config import logger

def predict(clf, X):
    try:
        predictions = clf.predict_proba(X)[:, 1]
        logger.info("Prediction successful.")
        return predictions
    except Exception as e:
        logger.error(f"Error during prediction: {e}")
        raise

def add_predictions_to_dataframe(data, predictions):
    try:
        data_with_predictions = data.assign(y_pred=np.round(predictions, 0))
        logger.info("Predictions added to dataframe successfully.")
        return data_with_predictions
    except Exception as e:
        logger.error(f"Error adding predictions to dataframe: {e}")
        raise
