import logging 
import datetime
import os 

filename = f'{datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")}.log'

log_path = os.path.join(os.getcwd(), "logs")

os.makedirs(log_path , exist_ok= True)

file_path = os.path.join(log_path , filename)

logging.basicConfig(level=logging.INFO , filename= file_path , 
                    format= '[(%asctime)s] %(lineno)d %(name)s %(levelname)s - %(message)s')