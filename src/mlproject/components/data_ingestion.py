import os
import sys
from src.mlproject.exception import CustomException
from src.mlproject.logger import logging
import pandas as pandas
from src.mlproject.utils import read_sql_data
from sklearn.model_selection import train_test_split

from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    train_data_path:str=os.path.join('artifacts','train.csv')
    test_data_path:str=os.path.join('artifacts','test.csv')
    raw_data_path:str=os.path.join('artifacts','raw.csv')

class DataIngestion:
    def __init__(self):
        self.initiate_config=DataIngestionConfig()

    def initiate_data_ingestion(self):
        try:
            ## reading code 
            df=read_sql_data()
            logging.info("reading data from mysql database")

            ## creating the atrifact folder.
            os.makedirs(os.path.dirname(self.initiate_config.train_data_path),exist_ok=True)
            df.to_csv(self.initiate_config.raw_data_path,index=False,header=True)

            ## Splitting data into training and testing data.
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)

            ## Saving training and testing data in their right path.
            train_set.to_csv(self.initiate_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.initiate_config.test_data_path,index=False,header=True)

            logging.info("Data Ingestion is completed")

            return(self.initiate_config.train_data_path,self.initiate_config.test_data_path)

        except Exception as e:
            raise CustomException(e,sys)
