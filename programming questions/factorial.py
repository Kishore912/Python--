def factorial(num):
    n=1
    for i in range(1,num+1):
        n=n*i
    print(n)    

factorial(int(input()))