# METACHARACTERS

import re
txt="hi there is a moment 59"
x=re.findall("[h-t]",txt)
print(x)
y=re.findall("\d",txt)
print(y)
z=re.findall("t...e",txt)
print(z)
a=re.findall("^hi",txt)
print(x)
b=re.findall("59$",txt)
print(b)
c=re.findall("hi.*59",txt)
print(c)
d=re.findall("there.+59",txt)
print(d)
e=re.findall("m.{4}t",txt)
print(e)
f=re.findall("t.?e",txt)
print(f)
g=re.findall("59|46",txt)
if g:
    print("59 is present")
else:
    print("46 is present")    