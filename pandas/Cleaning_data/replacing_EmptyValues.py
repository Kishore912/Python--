import pandas as pd
E = pd.read_csv('D:/kishore/python/pandas/data.csv')

# E.fillna(5000,inplace=True)
# print(E.to_string())

#replace nan values in a specified columns

E["Calories"].fillna(2000,inplace=True)
print(E.to_string())

# replace nan values using MEAN
# X= E["Calories"].mean()
# E['Calories'].fillna(X,inplace=True)
# print(E.to_string())

#replacing nan values using MEDIAN
# X= E["Calories"].median()
# E['Calories'].fillna(X,inplace=True)
# print(E.to_string())

#replacing nan values using MODE

# X= E["Calories"].mode()[0]
# E['Calories'].fillna(X,inplace=True)
# print(E.to_string())
