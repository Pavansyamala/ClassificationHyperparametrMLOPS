import os 
import sys
from src.logger.custom_logging import logging

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

logging.info("information 1")