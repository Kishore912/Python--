import pandas as pd
df = pd.read_csv('D:/kishore/python/pandas/data.csv')
print(df)    # printing only df will give first 5 rows and last 5 rows
print('')

#----------------------------------------------------------------

print(df.to_string())        # using to_string() you can display entire data frames
print(" ")
#-------------------------------------------------

max_row = pd.options.display.max_rows
print(max_row)