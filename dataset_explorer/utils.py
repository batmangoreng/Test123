from datetime import datetime
import pandas as pd
import os


def get_current_datetime():
    
    # datetime object containing current date and time
    now = datetime.now()
         
    # dd/mm/YY H:M:S
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    return dt_string


def create_error_file(output_path):
  errors_df = pd.DataFrame(error_file, columns=['FILENAME', 'DESCRIPTION', 'TIMESTAMP'])
  excel_writer = pd.ExcelWriter(output_path+"\\" +'errors.xlsx', engine='openpyxl')
  errors_df.to_excel(excel_writer, sheet_name='Log')
  excel_writer.close()

    

def log_error(f, message):
    error = (f, message, get_current_datetime())
    error_file.append(error)

  
def create_error_file(output_path):
  errors_df = pd.DataFrame(error_file, columns=['FILENAME', 'DESCRIPTION', 'TIMESTAMP'])
  excel_writer = pd.ExcelWriter(output_path+"\\" +'errors.xlsx', engine='openpyxl')
  errors_df.to_excel(excel_writer, sheet_name='Log')
  excel_writer.close()

def init_result_file():
    global result_file
    result_file = []

def init_error_file():
    global error_file
    error_file = []
