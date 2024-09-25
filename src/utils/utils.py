import os 
import sys 
import pickle 

from src.logger.custom_logging import logging 
from src.exception.exception import CustomException 

def load_object(path):
    try:
        with open(path, 'rb') as file:
            return pickle.load(file)
        logging.info(f"Succesfully loaded Object from the path {path}")
    except Exception as e:
        logging.info(e)
        raise CustomException(e , sys)


def save_object(path , obj):
    try :

        dirname , ext = os.path.split(path)
        if dirname :
            os.makedirs(dirname , exist_ok=True)
        
        with open(path, 'wb') as file:
            pickle.dump(obj, file) 
        
        logging.info(f"Object Created Succesfully at the path : {path}")

    except Exception as e : 
        logging.info(e)
        raise CustomException(e , sys)