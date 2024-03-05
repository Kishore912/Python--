n=int(input())
k=n-1
for i in range(n):
    for j in range(k):
        print(" ",end=" ")
    k=k-1
    for j in range(0,i+1):
        print("* ",end=" ")
    print("\r")        