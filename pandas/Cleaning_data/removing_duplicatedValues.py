import pandas as pd
df = pd.read_csv('D:/kishore/python/pandas/data.csv')

#to check if the given data set contains duplicate or not 
#it will return boolean values True or False

# E=df.duplicated()
# print(E.to_string())

df.drop_duplicates(inplace=True) # if you are not assigning it to df then do inplace=True or df = df.drop_duplicates()
print(df.to_string())