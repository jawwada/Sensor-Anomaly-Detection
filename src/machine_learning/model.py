from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.gaussian_process.kernels import RBF
from config.log_config import logger

def train_model(X_train, y_train):
    try:
        clf = GaussianProcessClassifier(1.0 * RBF(1.0))
        clf.fit(X_train, y_train.ravel())
        logger.info("Model training successful.")
        return clf
    except Exception as e:
        logger.error(f"Error in model training: {e}")
        raise

def evaluate_model(clf, X_test, y_test):
    try:
        score = clf.score(X_test, y_test)
        logger.info(f"Model evaluation successful. Score: {score}")
        return score
    except Exception as e:
        logger.error(f"Error in model evaluation: {e}")
        raise
