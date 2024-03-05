import pandas as pd
data = {
    'cars':['bmw','benz','mini'],
    'bike':['RE','benili','R15']
}
print(pd.DataFrame(data))


#------------------------------------------------------------

lock = pd.DataFrame(data,index=['performance','luxury','compact'])
print(lock)

#--------------------------------------------------------------

print(lock.loc[['performance','compact']])