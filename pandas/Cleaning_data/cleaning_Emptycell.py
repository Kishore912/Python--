import pandas as pd
E = pd.read_csv('D:/kishore/python/pandas/data.csv')

# E.dropna(inplace=True)
# print(E.to_string())

# -------------------------------------

# removing row that contain nan value using a specific column

E.dropna(subset=["Calories"],inplace=True)
print(E.to_string())