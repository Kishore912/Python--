def median_no(num):

    num.sort()
    n=len(num)
    if(n%2==0):
        median1=num[n//2]
        median2=num[n//2+1]
        median=(median1+median2)//2
        print(median)
    else:
        median=num[n//2]
        print(median)    
num=list(map(int,input().strip().split()))
median_no(num)