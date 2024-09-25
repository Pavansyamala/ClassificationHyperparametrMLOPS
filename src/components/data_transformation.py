import os 
import sys 

from src.exception.exception import CustomException 
from src.logger.custom_logging import logging 

import pandas as pd
import numpy as np
from sklearn.compose import ColumnTransformer 
from sklearn.preprocessing import StandardScaler , MinMaxScaler 
from dataclasses import dataclass 

import pickle


@dataclass 
class DataTransformationConfig:
    def __init__(self):
        self.preprocessor_path = 'artifacts/preprocessor.pkl'

class DataTransformation:

    def __init__(self , train_path):
        self.train_path = train_path
        self.trans_config = DataTransformationConfig()
        logging.info("Initializing DataTransformation")
    
    def initiate_data_transformation(self):
        try :
            logging.info("Loading the Training Data") 

            data = pd.read_csv(self.train_path) 

            features = ['Square_Footage','Num_Bedrooms','Num_Bathrooms','Year_Built','Lot_Size','Garage_Size','Neighborhood_Quality']
            labels = ['House_Price']

            x = data[features]
            y = data[labels]

            
            logging.info("Creating Preprocessor for training")
            ct1 = ColumnTransformer([('Scaling' , MinMaxScaler() , ['Square_Footage' , 'Lot_Size'])] , remainder = 'passthrough') 

            logging.info("initiating preprocess for training")
            x_transformed = ct1.fit_transform(x)

            dirname = os.path.dirname(self.trans_config.preprocessor_path)

            os.makedirs(dirname , exist_ok=True) 

            with open(self.trans_config.preprocessor_path , 'wb') as file:
                pickle.dump(ct1 , file=file)
            
            logging.info("Saved Preprocessor object")
            logging.info("Preprocessing Completed")

            return x_transformed , y.values

        except Exception as e:
            logging.info(e)
            raise CustomException(e,sys)