a=int(input("enter no"))
b=int(input("enter no"))
for i in range(b,a-1,-1):
    for j in range(a,i+1):
        print(j,end=" ")
    print(" ")  