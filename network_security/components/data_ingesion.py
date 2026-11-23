from network_security.entity.config_entity import DataIngestionConfig
from network_security.exception import NetworkSecurityException
from network_security.logging.logger import logging

# configuration for data ingestion config

import os
import sys
import pandas as pd
import numpy as np
import pymongo
from typing import List
from sklearn.model_selection import train_test_split
from dotenv import load_dotenv
load_dotenv()

MONGO_DB_URL = os.getenv("MONGO_DB_URL")

class DataIngestion:
    def __init__(self, data_ingestion_config:"DataIngestionConfig"):
        try:
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise NetworkSecurityException(e, sys) from e

    def export_collection_as_dataframe(self):
        """reads data from mongoDB collection"""
        try:
            database_name = self.data_ingestion_config.database_name
            collection_name = self.data_ingestion_config.collection_name
            self.mongo_client = pymongo.MongoClient(MONGO_DB_URL)
            collection = self.mongo_client[database_name][collection_name]


            df=pd.DataFrame(list(collection.find()))
            if "_id" in df.columns:
                df=df.drop("_id",axis=1)

            df.replace({"na":np.nan},inplace=True)
            return df
        
        except Exception as e:
            raise NetworkSecurityException(e, sys) from e


    def export_data_into_feature_store(self,dataframe:pd.DataFrame):
        """export data into feature store"""
        try:
            feature_store_file_path=self.data_ingestion_config.feature_store_file_path
            dir_path=os.path.dirname(feature_store_file_path)
            #create a folder 
            os.makedirs(dir_path,exist_ok=True)
            dataframe.to_csv(feature_store_file_path,index=False,header=True)
            return dataframe
        except Exception as e:
            raise NetworkSecurityException(e, sys) from e
        


    def initiate_data_ingestion(self):
        try:
            dataframe=self.export_collection_as_dataframe()
            dataframe=self.export_data_into_feature_store(dataframe)



        except Exception as e:
            raise NetworkSecurityException(e, sys) from e


    def split_data_as_train_test(self,dataframe:pd.DataFrame):
        """split the data into train and test"""
        try:
            train_set,test_set=train_test_split(dataframe,test_size=self.data_ingestion_config.training_test_split_ratio)
            logging.info("performed train test split on the data")
            logging.info(f"train set: {train_set.shape} and test set: {test_set.shape}")
            logging.info("Exited the split_data_as_train_test method of DataIngestion class")
            train_file_path=self.data_ingestion_config.training_file_path
            test_file_path=self.data_ingestion_config.testing_file_path

            #create folder if not available
            logging.info(f"Exporting train and test data into feature store")
            os.makedirs(os.path.dirname(train_file_path),exist_ok=True)
            
            os.makedirs(os.path.dirname(test_file_path),exist_ok=True)

            train_set.to_csv(train_file_path,index=False,header=True)
            test_set.to_csv(test_file_path,index=False,header=True)
            logging.info(f"Exported train and test data into feature store")

        except Exception as e:
            raise NetworkSecurityException(e, sys) from e

        
        

