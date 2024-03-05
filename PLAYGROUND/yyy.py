n = int(input())
arr = map(int, input().split())
list1=list(arr)
x = len(list1)

previous_max=max(list1)   #4
list1.remove(previous_max)   #list1=[1,2,3,4,4,4]
for i in range(x):
    current_max = max(list1) #3
    if(previous_max == current_max):
        list1.remove(current_max)      #list1=[1,2,3]
print(current_max)   
