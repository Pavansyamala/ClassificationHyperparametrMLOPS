import os 
import sys
from src.logger.custom_logging import logging
from src.exception.exception import CustomException 
from src.utils.utils import load_object  
from sklearn.metrics import r2_score , mean_squared_error

import mlflow 


class modelEvaluvation:
    def __init__(self , test_x , test_y , model_path):
        
        self.test_x = test_x
        self.test_y = test_y
        self.model_path = model_path 
    
    def initiateModelEvaluation(self):

        with mlflow.start_run():
            
            self.model = load_object(self.model_path) 
            predictions = self.model.predict(self.test_x) 

            accuracy = r2_score(predictions , self.test_y)
            loss = mean_squared_error(predictions , self.test_y) 

            mlflow.log_metrics({'accuracy':accuracy, 'loss':loss})

            logging.info("Accuracy of the model is {accuracy}".format(accuracy=accuracy)) 
            logging.info("Loss of the model is {loss}".format(loss=loss)) 

            # mlflow.sklearn.log_model(self.model , "model_mlflow")