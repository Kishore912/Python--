def fibonacci_series(num):
    n1=int(input("enter first no: "))
    n2=int(input("enter second no: ")) 
    print(n1,n2,end=" ")
    for i in range(2,num):
        n3=n1+n2
        n1=n2
        n2=n3
        print(n3,end=" ")
fibonacci_series(int(input()))    