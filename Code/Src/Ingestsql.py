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
    # Configuration files used to read Paths using Yaml Library
    # MYSQL
        # conda install -c anaconda mysql-connector-python
        # pip3 install mysql-connector-python
        # pip3 install PyMySQL


# Library
import pandas as pd  # Data ingestion and manipulation
import numpy as np   # Numerical computation
import mysql.connector  # MYSQL connector

# MySQL Connection parameters 
mysql_host = input('Enter the hostname: ') # Name of the host
mysql_user = input('Enter the username: ') # Name of user in db
mysql_password = input('Enter the password: ') # Password details
mysql_database = input('Enter the name of database: ') # Schema name


#use the above details of connection parameters to connect with mysql database
mysql_connection = mysql.connector.connect(
    host=mysql_host,
    user=mysql_user,
    password=mysql_password,
    database=mysql_database
)

storagepath=input("Enter the name of storage path: ") # Path to store ingested file 

# Ingest datatable 1
SQL_QUERY=input("Enter the SQL query for data from mysql table: ")  # SQL query written in python environment
df = pd.read_sql(SQL_QUERY, con=mysql_connection) # Read the data from MYSQL using the above query
df.to_csv(storagepath+'Ingest_Sql.csv',index=False)  # Store ingested data as excel on local CWD

# --------------------------------- End of code ---------------------------------------------------------
