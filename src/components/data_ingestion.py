import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

from src.logger.custom_logging import logging
from src.exception.exception import CustomException 
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer

from dataclasses import dataclass

import os
import sys 

@dataclass
class DataConfig:
    def __init__(self):
        self.raw_data_path = 'artifacts/raw_data.csv'
        self.train_data_path = 'artifacts/train_data.csv'
        self.test_data_path = 'artifacts/test_data.csv' 


class DataIngestion:

    def __init__(self):
        self.config = DataConfig() 

        logging.info("Initiating the DataIngestion")
        
    def initiate_data_ingestion(self):

        try : 
            
            raw_path = self.config.raw_data_path 
            train_path = self.config.train_data_path
            test_path = self.config.test_data_path

            dirname , filename = os.path.split(raw_path) 

            if dirname:
                os.makedirs(dirname , exist_ok=True)
            
            
            path = "D:\\InfosysCertificates\\archive (3)\\house_price_regression_dataset.csv"
            data = pd.read_csv(path)
            data.to_csv(raw_path) 
            logging.info("Raw Data Saved")
            
            logging.info("Data spitting started")
            train_data , test_data = train_test_split(data , train_size = 0.7 , random_state = 42)
            logging.info("Data Splitting Finished")

            logging.info("Training Data Saving Started")
            train_data.to_csv(self.config.train_data_path)
            logging.info("Training Data Saving finished")

            logging.info("Testing Data Saving Started")
            test_data.to_csv(self.config.test_data_path) 
            logging.info("Testing Data Saving finished") 

            logging.info("Data Ingestion Completed")  

            return train_path , test_path 
        
        except Exception as e:
            logging.info(e)
            raise CustomException(e,sys) 

        

if __name__ == "__main__":
    obj = DataIngestion()
    train_path , test_path = obj.initiate_data_ingestion()
    obj2 = DataTransformation(train_path , test_path)
    x , y , xt , yt = obj2.initiate_data_transformation()

    obj3 = ModelTrainer(x,y,xt,yt)

    obj3.initiate_model_training()


        

        
