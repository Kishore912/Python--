i=0
while i<10:
    print(i)
    i+=1

#----------------------------------------

i=10
while i<15:
    print(i)
    if i==12:
        break
    i+=1

#-----------------------------------------------------

i=20
while i<28:
    i+=1  
    if i==26:
        continue
    print(i)


#-------------------------------------------------------

a=0
while a<10:
    a+=1
    if a==5:
        continue
    print(a)    




count=0
prime=1
num=7
while(prime<=num):
    if(num%prime==0):
        count+=1
        prime+=1   

if count==2:
    print("prime")
else:
    print("not a prime")             