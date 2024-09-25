import sys
import numpy as np
import pandas as pd 

from src.exception.exception import CustomException 
from src.logger.custom_logging import logging 

from src.utils.utils import load_object  


class PredictionPipeline:

    def __init__(self , pred_data):
        self.model_path = "D:\Mlops\\artifacts\\best_model.pkl"
        self.preprocesser_path = "D:\\Mlops\\artifacts\\preprocessor.pkl"
        self.pred_data = pred_data 
    

    def initiate_prediction_pipeline(self):

        try:

            logging.info("Starting prediction pipeline")

            logging.info("Loading Trained Model") 
            model = load_object(self.model_path)
            logging.info("Succesfully Loaded Trained Model")

            logging.info("Loading Preproceesing Object") 
            preprocessing = load_object(self.preprocesser_path)
            logging.info("Succesfully Loaded Preprocessing Object")

            preprocessed_data = preprocessing.transform(self.pred_data) 
            prediction = model.predict(preprocessed_data) 

            logging.info("Prediction Completed Successfully")

            return prediction[0][0]

        except Exception as e:
            logging.info(e)
            raise CustomException(e,sys) 


if __name__ == "__main__":

    data = pd.read_csv("D:\\Mlops\\artifacts\\raw_data.csv")
    features = ['Square_Footage','Num_Bedrooms','Num_Bathrooms','Year_Built','Lot_Size','Garage_Size','Neighborhood_Quality']
    features = data[features]
    data = features.iloc[0:1,:]

    obj = PredictionPipeline(data)
    obj.initiate_prediction_pipeline()
        
