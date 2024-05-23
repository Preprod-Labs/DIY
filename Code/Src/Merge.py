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
        # MYSQL: Yes
        # NoSQL: No
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

# Library
import pandas as pd  # Data ingestion and manipulation
import numpy as np   # Data manipulation

#path of SQL and Mongo csv ingested files (processed folder)
path=input( "enter the path of sql and mongo data files: ")

# Read SQL file
DB1=pd.read_csv(path+'Ingest_Sql.csv')
print(DB1.info())

# Read Mongo file 

DB2=pd.read_csv(path+'ingest_mongo.csv')
print(DB2.info())
# Merge both data tables
DB2.drop('_id',axis=1,inplace=True)
print(DB2.info())
D1 = pd.merge(DB1,DB2, on=['Customer_ID'], how="inner")
print(D1.info())

DB=D1.copy(deep=True) # Backup the original data  # Backup dataset
DB.to_csv(path+'merged.csv',index=False) # store the merged file in the same path as ingested file ( processed folder)

# --------------------------------- End of code ---------------------------------------------------------