import pandas as pd

A={
    "cars":"BMW",
    "bikes":"R15"
}
a=pd.Series(A)
print(a)

#------------------------------------------

B=[1,2,3,4]
b=pd.Series(B)
print(b)

#-------------------------------

C=[1,2,3,4]
c=pd.Series(C,index=["X","Y","Z","P"])
print(c)

#--------------------------------------

print(c["X"])