import logging
import datetime
import os

# Generate a timestamped log file name
filename = f'{datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")}.log'

# Create a logs directory in the current working directory
log_path = os.path.join(os.getcwd(), "logs")

# Create the logs directory if it doesn't exist
os.makedirs(log_path, exist_ok=True)

# Create the full path for the log file
file_path = os.path.join(log_path, filename)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    filename=file_path,
    format='[%(asctime)s] %(lineno)d %(name)s %(levelname)s - %(message)s'
)


