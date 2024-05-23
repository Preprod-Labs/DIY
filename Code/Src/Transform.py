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
     
    # Description: This code enables data transformation on merged file
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

#Import Libraries
import numpy as np  # numerical computation library
import pandas as pd # data manipulation library
from sklearn.preprocessing import LabelEncoder # Encode labels 

path=input(" Enter the path of merged file csv location: ")

df_merge=pd.read_csv(path+'merged.csv')

#1. Convert categorical to numerical
categorical_col=['Gender','Country', 'Country_Code']

#save as category type for the features which need label encoding 
def obj2cat(data):
    for col in categorical_col:
        data[col]=data[col].astype('category')
    return data

def cat2num(data):
    le = LabelEncoder()
    for col in categorical_col:
        data[col]=le.fit_transform(data[col])

#2. Remove special characters in price feature

specialchar_col=['Price']

def specialchar(data):
    for col in specialchar_col:
        data[col]=data[col].str.replace("$","")
        data[col]=data[col].astype('float64')
    return data

#3. Perform transformation by calling the previous functions from step 1 and 2

def transform(data):
    specialchar(data),
    obj2cat(data),
    cat2num(data)
    return data

#4. Save the transformed values in a dataframe

df_transform=transform(df_merge)

#OPTIONAL: TO REPLACE ZERO VALUES IN PRICE AND NO OF UNITS SOLD AS IT GENERALLY PERFORMED BASED ON MODEL PERFORMANCE

price_col = df_transform['Price']
price_col.replace(to_replace = 0, value = price_col.median(), inplace=True)

units_col = df_transform['No_of_units_sold']
units_col.replace(to_replace = 0, value = units_col.median(), inplace=True)

#5. Save the transformed file to load into datalake / datawarehouse

df_transform.to_csv(path+'transform.csv',index=False)

# --------------------------------- End of code ---------------------------------------------------------


