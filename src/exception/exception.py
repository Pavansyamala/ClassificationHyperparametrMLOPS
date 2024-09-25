import os 
import sys 


class CustomException(Exception):

    def __init__(self , error_msg , error_details:sys):
        self.error_msg = error_msg
        _,_, exc_tb = error_details.exc_info()

        self.lineno = exc_tb.tb_lineno 
        self.filename = exc_tb.tb_frame.f_code.co_filename
    
    def __str__(self):

        return f'Error Occured in Line no : {self.lineno} in the file name : {self.filename} and the details pf the error as follows : {self.error_msg}'
    

