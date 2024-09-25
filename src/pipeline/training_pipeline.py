import os 
import sys 

from src.exception.exception import CustomException 
from src.logger.custom_logging import logging 
from src.components.data_ingestion import DataIngestion 
from src.components.data_transformation import DataTransformation 
from src.components.model_trainer import ModelTrainer 
from src.utils.utils import load_object 


class TrainingPipeline:
    def __init__(self , path):
        self.data_path = path

    def initiate_training_pipeline(self):

        try :

            logging.info("Training Pipeline Started")

            ingestion = DataIngestion(self.data_path)
            training_path , testing_path = ingestion.initiate_data_ingestion()

            transformation = DataTransformation(training_path,testing_path) 
            x,y , xt , yt = transformation.initiate_data_transformation()

            model_training = ModelTrainer(x,y,xt , yt)

            model_path = model_training.initiate_model_training()

            logging.info(f"Training Pipeline Finished and Model is succesfully saved at the location {model_path}")


        except Exception as e :
            logging.info(e)
            raise CustomException(e , sys)

if __name__ == "__main__": 

    path =  "D:/InfosysCertificates/archive (3)/house_price_regression_dataset.csv"

    obj = TrainingPipeline(path=path)
    obj.initiate_training_pipeline()
        