#this is for exception handling purposeses 
import sys
import logging 

def error_message_detail(error,error_detail:sys):
   _,_, exc_tb= error_detail.exc_info  #for getting the execution info it provided 3 info last one will give specific loc of exception
   file_name = exc_tb.tb_frame.f_code.co_filename 
   error_message = "Error occured in python script [{0}] line number [{1}] and error message [{2}]".format(
      file_name, exc_tb.tb_lineno, str(error)
   )
   return error_message
   
class CustomException(Exception):
   def __init__(self,error_message, error_detail: sys):
      super().__init__(error_message) #since we are inheriting from exception
      self.error_message = error_message_detail(error_message,error_detail=error_detail)

   def __str__(self):
      return self.error_message #used for printing the error message
   


     