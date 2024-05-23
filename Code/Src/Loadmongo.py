# META DATA - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

    # Developer details: 
        # Name: Harish S
        # Role: Architect
        #  Code ownership rights: Harish S
    # Version:
        # Version: V 1.0 (19 Mar 2024)
            # Developer: Harish S
            # Unit test: Pass
            # Integration test: Pass
     
    # Description: This code enables data load to mongo db from an external data sources.
        # MYSQL: No
        # NoSQL: Yes
        # MQs: Implemented in a seprate code
        # Cloud: To be implemented
        # Data versioning: No
        # Data masking: Yes

# CODE - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# Dependency: 
    # Environment:     
        #Python 3.10.13
        #Numpy 1.26.1
        #Pandas 2.2.1
    # Configuration files used to read Paths using Yaml Library
    # Mongo Library installation :
       # pip install pymongo


import numpy as np  # Library for numerical computation                   
import pandas as pd # Library for data manipulation
import pymongo      # Library to connect python environment with mongodb
from pymongo import MongoClient # client which connects python environment

# Mongo Connection parameters 
mongo_host = input('Enter the hostname: ')
mongo_port = int(input('Enter the port: '))
mongo_database = input('Enter the name of database : ')
mongo_collection = input('Enter the name of collection : ')

#use the above details of connection parameters to connect with mysql database

mongo_client = MongoClient(mongo_host, mongo_port) # Mongo client holds the details of host and port name
mongo_db = mongo_client[mongo_database] # Mongo client connects to database in the mongo database
mongo_col = mongo_db[mongo_collection]  # Mongo client connects to collection in the mongo database

# Load your dataset from CSV's
dataset_path = input(' Enter the path of CSV file: ') # enter the path where csv file is located 
df1=pd.read_csv(dataset_path+'mongodata.csv') # read the data into dataframe

# Select the columns into which csv data has to be loaded
mong_col = ['Customer_ID', 'Customer_Name', 'Email', 'Gender', 'City', 'Car_Make','Country', 'Country_Code']

data_dict = df1[mong_col].to_dict(orient='records') # convert the dataframe to dictionary
mongo_col.insert_many(data_dict) # Insert the data into collection in Mongodb
mongo_client.close() #close the mongodb connection

# --------------------------------- End of code ---------------------------------------------------------