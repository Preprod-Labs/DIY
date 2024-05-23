# welcome to PPC DIY project 

This is a readme file available in feature branch in git

please follow below instructions as below

This project is performing basic data engineering operations on car sales data 

the source data to be loaded to mysql and mongo db is present in Data folder ->  Master
the files generated as a result of data engineering steps is present in Data folder -> Processed

How to execute the project

#1. In data folder -> mysqldata.csv and mongodata.csv to be loaded into respective databases by executing
the script files Loadsql.py and Loadmongo.py which are present in Code -> Src folder

#2. once csv files are loaded into mysql and mongodb perform ingestion operation by executing the script files ingestsql.py and ingestmongo.py which are present in Code -> Src folder

#3. Once ingestion of both csv files are done , perform merge operation by executing the script file merge.py which is present in Code -> Src folder

#4. Once merge of both sql and mongo data is done, transformation steps is performed by executing the script file transform.py which is present in Code -> Src folder

#5. Once transformation is done , load the transformed file by executing the script file load.py which is present in Code -> Src folder

Note: the connection parameters such as username and password for mysql to be defined by you

host for mysql and mongodb is localhost
port no of mongodb is 27017

Please note:

1. Infrastructure set up files are provided to install mysql and mongodb

2. set up anaconda  and create a seperate environment by folling steps in https://docs.anaconda.com/free/navigator/tutorials/manage-environments.html

3. Python version is mentioned in code files which can be downloaded while creating the new environment

4. other library versions can be reffered from requirements.txt which is provided here 

please note : do not install all libraries at once from requirements.txt which is only for references