n = list(map(int,input().strip().split()))
target = int(input())

def binary_search(n,target):
    left,right = 0,len(n)-1
    n.sort()
    result = -1

    while left<=right:

        mid = left+(right-left)//2

        if n[mid] == target:
            result = mid
            left = mid+1
        elif n[mid]<target:
            left = mid+1
        else:
            right = mid-1
    return result

final = binary_search(n,target)
print(n)
print(final)                