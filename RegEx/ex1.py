import re
txt="hi this is kishore"
x=re.findall("this",txt)
y=re.findall("^hi.*kishore$",txt)
print(x)
print(y)


#------------------------------------------------------------------

import re
txt="hey whatsup bro doing good?"
a=re.findall("kishore",txt)
print(a)
if a:
    print("yes there is a match")
else:
    print("no match found")    