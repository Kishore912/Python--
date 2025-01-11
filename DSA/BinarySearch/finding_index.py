n = list(map(int,input().strip().split()))
target = int(input())

def binary_search(n,target):
    n.sort()
    left = 0
    right = len(n)-1

    while left<=right:

        mid = left+(right-left)//2

        if n[mid] == target:
            return mid
        
        elif n[mid]<target:
            left = mid+1

        else:
            right = mid-1
            
    return -1

result=binary_search(n,target)

if result!=-1:
    print(f"{target} is found at index {result}")          
else:
    print(f"{target} not found in the array")      