N=int(input())
sum=0
while N>0:
    sum+=N%10 #gives the remainder which means the last letter in N
    N=N//10  #once we got the last letter it should be removed 
print(sum)    