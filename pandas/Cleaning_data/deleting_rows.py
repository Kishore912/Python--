import pandas as pd
df = pd.read_csv('D:/kishore/python/pandas/data.csv')

for i in df.index:
    if df.loc[i,"Duration"]<40:
        df.drop(i,inplace=True)
           
print(df.to_string())  
      