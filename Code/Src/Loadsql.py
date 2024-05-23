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

import pandas as pd #data manipulation library
import mysql.connector #connector library between python and mysq;

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

# Load your dataset from CSV's
dataset_path = input(' Enter the path of CSV file: ') # enter the path where csv file is located 
df1=pd.read_csv(dataset_path+'mysqldata.csv') # read the data into dataframe

# Insert data into MySQL table1
mysql_cursor = mysql_connection.cursor() #initiate the connection via cursor which pin point the schema and execute SQL query on python environment

#Load the data from dataframe into mysql table row by row
for index, row in df1.iterrows():
    insert_query = "INSERT INTO priceinfo (Customer_ID,Purchase_Date,No_of_units_sold,Car_model_year,Price) VALUES (%s, %s,%s,%s,%s)"
    values = tuple(row)
    mysql_cursor.execute(insert_query, values)

mysql_connection.commit()               # once loaded commit into database to save the data
mysql_cursor.close()                    # Close the mysql cursor connection
mysql_connection.close()                # Close the connection between python environment and mysql

# --------------------------------- End of code ---------------------------------------------------------