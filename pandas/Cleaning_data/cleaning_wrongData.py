import pandas as pd
df = pd.read_csv('D:/kishore/python/pandas/data.csv')

#for replacing a single a value in a small data set 

# df.loc[79,"Duration"] = 45
# print(df.to_string())

#for replacing a values in a large data set
#we can use conditions in forloop

for i in df.index:
    if df.loc[i,"Duration"]>45:
        df.loc[i,"Duration"] = 45

print(df.to_string())        