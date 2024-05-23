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
     
    # Description: This code enables data ingestion from an external data sources.
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

#load the libraries
import pandas as pd # Library for data manipulation
import numpy as np  # Library for numerical computation   
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


#access mong database and client through mongo client 
temp_db=mongo_col # store the values of collection in temporary variable
cursor=temp_db.find() #cursor points to the specific collection mentioned by temp_db
entries=list(cursor)  #convert the values of collection into list and store it in entries
mongo_client.close()  #close the mongo connection

# load the list data into dataframe

ingestpath=input( "Enter the storage path: ") # enter the path to save csv file
df=pd.DataFrame(entries) # load the entries into dataframe
df.to_csv(ingestpath+'ingest_mongo.csv',index=False) #save dataframe as csv file

# --------------------------------- End of code ---------------------------------------------------------