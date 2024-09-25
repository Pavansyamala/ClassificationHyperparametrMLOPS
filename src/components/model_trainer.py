import os 
import sys 

from src.logger.custom_logging import logging 
from src.exception.exception import CustomException 
from src.utils.utils import train_models , evaluate_select_bestmodels , save_object

import pandas as pd
import numpy as np 

from sklearn.linear_model import LinearRegression , Lasso , Ridge
from sklearn.tree import DecisionTreeRegressor 
from sklearn.ensemble import RandomForestRegressor , GradientBoostingRegressor 

from dataclasses import dataclass 


@dataclass 
class ModelTrainerConfig:
    def __init__(self):
        self.model_path = 'artifacts/best_model.pkl'


class ModelTrainer:
    def __init__(self , x_train , y_train , x_test , y_test):
        self.model_trainer_config = ModelTrainerConfig()
        self.x_train = x_train
        self.y_train = y_train
        self.x_test = x_test 
        self.y_test = y_test 
    
    def initiate_model_training(self):
        try:
            logging.info(" Model Training File Initiated : ")

            models_dict = {
                'LinearRegression' : LinearRegression(),
                'LassoRegression' : Lasso(),
                'Ridge' : Ridge(), 
                'DecisionTreeRegressor' : DecisionTreeRegressor(),
                'RandomForestRegressor' : RandomForestRegressor(),
                'GradientBoostingRegressor':GradientBoostingRegressor()
            } 

            trained_models = train_models(models_dict , self.x_train, self.y_train) 

            models_accuracy , best_model = evaluate_select_bestmodels(trained_models , self.x_test, self.y_test)

            for i in models_accuracy :
                logging.info(f'{i} model accuracy is : {models_accuracy[i]}')

            logging.info("Saving the best model") 

            save_object(self.model_trainer_config.model_path , best_model)

            logging.info(" Best Model Svaed Successfully ")

            logging.info(" Model Training File Finished ")

            return self.model_trainer_config.model_path 

        except Exception as e:
            logging.info(e)
            raise CustomException(e,sys)
        
