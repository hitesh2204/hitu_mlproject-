from src.mlproject.exception import CustomException
from src.mlproject.logger import logging
import sys
from src.mlproject.components.data_ingestion import DataIngestion

if __name__=="__main__":
    logging.info("Th execution has started")

    try:
        data_ingestion=DataIngestion()
        data_ingestion.initiate_data_ingestion()
    
    except Exception as e:
        raise CustomException(e,sys)
