import os 
import sys 
import pickle 

from src.logger.custom_logging import logging 
from src.exception.exception import CustomException
from sklearn.linear_model import LinearRegression , Lasso , Ridge
from sklearn.tree import DecisionTreeRegressor 
from sklearn.ensemble import RandomForestRegressor , GradientBoostingRegressor 
from sklearn.metrics import r2_score  

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


def train_models(models , x_train , y_train):

    try :

        logging.info("Training of Models Started")

        for i in models:
            model = models[i]
            model.fit(x_train, y_train) 
            models[i] = model 

            logging.info(f" Trained Model {i} finihed")
        
        logging.info("Training of Models Finished")

        return models 
        
    
    except Exception as e :
        logging.info(e)
        raise CustomException(e,sys)

def evaluate_select_bestmodels(models , x_test , y_test):

    try :

        max_acc = -1e9 
        best_model = None 

        logging.info(" Started Evaluating all models and selecting best model")

        model_accuracy = {}

        for i in models:
            model = models[i]
            predicted = model.predict(x_test)
            model_accuracy[i] = r2_score(predicted, y_test) 
            if model_accuracy[i] > max_acc : 
                max_acc = model_accuracy[i] 
                best_model = model 
        
        logging.info(" Finished Evaluating all models and selected best model ")
        return model_accuracy , best_model 
    

    except Exception as e : 
        logging.info(e)
        raise CustomException(e , sys)

