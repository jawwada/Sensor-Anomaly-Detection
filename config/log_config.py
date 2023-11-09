import logging
from logging.handlers import RotatingFileHandler
import os

# Create logs directory if it does not exist
log_dir = "logs"
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

# Configure logging to output to both console and file
log_file = os.path.join(log_dir, 'sensor_fault_detection.log')

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Create handlers
console_handler = logging.StreamHandler()
file_handler = RotatingFileHandler(log_file, maxBytes=10000000, backupCount=5)

# Set level and format for handlers
console_handler.setLevel(logging.INFO)
file_handler.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# Get the root logger and add the handlers to it
logger = logging.getLogger()
#logger.addHandler(console_handler)
logger.addHandler(file_handler)

