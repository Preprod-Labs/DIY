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
     
    # Description: This code enables data load to mongo db from transform file
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


# import libraries

import numpy as np # Library for numerical computation
import pandas as pd # Library for data manipulation
from pymongo import MongoClient # Local connectivity client for mongo db

#path of the transformed csv file

path=input("Enter the path of transform file: ")
df = pd.read_csv(path+'transform.csv') # Read the transform file

Ldata=df.copy(deep=True) #perform deep copy of the transform file to Ldata variable to avoid changes to original dataframe

# connectivity to mongodb
mongo_host = input('Enter the hostname: ') # Hostname of MongoDB
mongo_port = int(input('Enter the port: ')) #Port of MongoDB
mongo_database = input('Enter the name of database : ') # Name of database to be used in mongodb
mongo_collection = input('Enter the name of collection : ') #Name of collection to be used in mongodb
mongo_client = MongoClient(mongo_host, mongo_port) # Mongo client holds the details of host and port name
mongo_db = mongo_client[mongo_database] # Mongo client connects to database in the mongo database
mongo_col = mongo_db[mongo_collection] # Mongo client connects to collection in the mongo database

#features from the dataset to be loaded to mongodb
col = ['Customer_ID', 'Purchase_Date', 'No_of_units_sold', 'Car_model_year',
       'Price', 'Customer_Name', 'Email', 'Gender', 'City', 'Car_Make',
       'Country', 'Country_Code']

#load the data into mongodb
data_dict = Ldata[col].to_dict(orient='records') # convert the dataframe to dictionary
mongo_col.insert_many(data_dict) # Insert the data into collection in Mongodb
mongo_client.close()  #close the mongodb connection

