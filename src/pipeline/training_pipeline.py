import os 
import sys 

from src.exception.exception import CustomException 
from src.logger.custom_logging import logging 
from src.components.data_ingestion import DataIngestion 
from src.components.data_transformation import DataTransformation 
from src.components.model_trainer import ModelTrainer 
# from src.utils.utils import load_object  
# from src.components.model_evaluation import modelEvaluvation 


class TrainingPipeline:
    
    def start_data_ingestion(self):
        try:
            path =  "D:/InfosysCertificates/archive (3)/house_price_regression_dataset.csv"
            data_ingestion = DataIngestion(path)
            training_path , testing_path = data_ingestion.initiate_data_ingestion()
            return training_path, testing_path 
        except Exception as e:
            raise CustomException(e,sys)
    
    def start_data_transformation(self,training_path,testing_path):
        try:
            data_tranformation = DataTransformation(training_path,testing_path)
            x,y,xt,yt = data_tranformation.initiate_data_transformation()
            return x,y,xt,yt
        except Exception as e:
            raise CustomException(e,sys)
    
    def start_model_training(self,x,y,xt,yt):
        try:
            model_trainer = ModelTrainer(x,y,xt,yt)
            model_path = model_trainer.initiate_model_training()
            return model_path 
        except Exception as e:
            raise CustomException(e,sys)
    
    def start_training(self):
        try:
            training_path , testing_path = self.start_data_ingestion()
            x,y,xt,yt = self.start_data_transformation(training_path,testing_path)
            model_path = self.start_model_training(x,y,xt,yt)
        except Exception as e:
            raise CustomException(e,sys)
    
        
    # def initiate_training_pipeline(self):

    #     try :

    #         logging.info("Training Pipeline Started")

    #         ingestion = DataIngestion(self.data_path)
    #         training_path , testing_path = ingestion.initiate_data_ingestion()

    #         transformation = DataTransformation(training_path,testing_path) 
    #         x,y , xt , yt = transformation.initiate_data_transformation()

    #         model_training = ModelTrainer(x,y,xt , yt)

    #         model_path = model_training.initiate_model_training()

    #         model_eval = modelEvaluvation(xt,yt,model_path) 
    #         model_eval.initiateModelEvaluation()

    #         logging.info(f"Training Pipeline Finished and Model is succesfully saved at the location {model_path}")


    #     except Exception as e :
    #         logging.info(e)
    #         raise CustomException(e , sys)

if __name__ == "__main__": 

    obj = TrainingPipeline()
    obj.start_training()
        