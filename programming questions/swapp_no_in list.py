# Python program to interchange first and last elements in a list

def swapp(num):
    n=len(num)
    temp=num[0]
    num[0]=num[n-1]
    num[n-1]=temp
    print(num)
list1=list(map(int,input().strip().split()))
swapp(list1)    