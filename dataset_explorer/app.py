import os 
import sys
import argparse
from pathlib import Path

from dataset_explorer import utils

import sweetviz as sv
import pandas as pd
from ydata_profiling import ProfileReport
import webbrowser
#import matplotlib
#matplotlib.use("svg")


output_path = r"C:\Users\e-um\AppData\Local\Temp" #os.path.join(os.path.expanduser('~'), 'Downloads')

def import_data(file):
       
    if file.endswith(".csv"):
        df = pd.read_csv(file, encoding='latin-1')
    elif file.endswith(".xlsx"):
        df = pd.read_excel(file)
    else: 
        utils.log_error(file, "The select file is not a .xlsx or .csv")
        print("ERROR - This type of file is not currently managed.")
        
    return df


def generate_report(file, mode):
    
    df = import_data(file)
    
    if not df.empty:
        if mode == 'Basic':  
        #    try:
                analyze_report = sv.analyze(df)
                report_path = output_path + r'/' + Path(file).stem + '_basic_' + 'report.html'
                analyze_report.show_html(report_path, open_browser=True)   
        #    except:
        #        utils.log_error(file, "The generation of the report has failed")
        #        print("ERROR - The generation of the report has failed.")
        elif mode == 'Advanced':
            #try:
                report_path = output_path + r'/' + Path(file).stem + '_advanced_' + 'report.html'
                design_report = ProfileReport(df)
                design_report.to_file(output_file=report_path)
                webbrowser.open_new_tab(report_path)
            #except Exception as e:
            #    utils.log_error(file, "The generation of the report has failed")
            #    print("ERROR - The generation of the report has failed.")
            #    print(e)


def main(file, mode):
    
      #print("[START]", flush=True)
      
      utils.init_error_file()
      
      print("> Generating data exploratory report...", flush=True)
      generate_report(file, mode)

      if utils.error_file == 0:    
          print("> Printing errors...")
          utils.create_error_file(output_path)
      
      #print("[END]", flush=True)
        
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Description de votre programme")
    parser.add_argument("-f","--folder",dest="folder", help="Chemin du fichier à traiter", required=True)
    args = parser.parse_args()
    main(args.folder)
    

