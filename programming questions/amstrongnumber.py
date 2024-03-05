def no_of_digits(num):
    count=0
    while num>0:
        count+= 1
        num=num//10
    return count    

def sum_of_squares(num,count):
    sum=0 
    while num>0:
        sum+=(num % 10)**count
        num=num//10
    return sum    
   


num=int(input())   
count=no_of_digits(num)
total_sum=sum_of_squares(num,count)
print("the given number is a amstrong number" if num == total_sum else "the given number is not a amstrong number")
