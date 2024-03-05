#  THE SEARCH() FUNCTION

import re
txt="the rain is heavy today"
x=re.search("the",txt)
print(x)
if x:
    print("there is a match")
else:
    print("there is no match found") 

#-----------------------------------------------------------

import re
start="there is been a mistake"
y=re.search("\s",start)   #returns the position of the first white space character
a=re.search("mapla",start)
print(y.start())     
print(a)

