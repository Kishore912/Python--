import pandas as pd
df = pd.read_csv('D:/kishore/python/pandas/data.csv')

print(df.head(10))       # will diplay first 10 rows
print(" ")                  
#------------------------------------------------------------
print(df.head())         #will display first 5  rows
print(" ")
#------------------------------------------------------------
print(df.tail(10))      #will display last 10 rows
print(" ")
#------------------------------------------------------------
print(df.tail())        # will display last 5 rows
print(" ")
#-------------------------------------------------------------
print(df.info())        # will give information about the data set