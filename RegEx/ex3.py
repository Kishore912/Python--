# THE SPLIT() FUNCTION

import re
txt="i cant see clearly when you are gone"
x=re.split("\s",txt)
y=re.split("\s",txt,2)
print(x)
print(y)

#----------------------------------------------------

# THE SUB() FUNCTION

import re
don="its been a long day"
c=re.sub("\s","9",don)
d=re.sub("\s","3",don,2)
print(c)
print(d)


#----------------------------------------------------------