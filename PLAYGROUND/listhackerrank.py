if __name__ == '__main__':
    N = int(input())
listt=[]
for i in range(0,N):
    cmd, *args = input().split()
    args = list(map(int, args))  
    if cmd=="insert":
        listt.insert(*args)
    elif cmd =="print":
        print(listt) 
    elif cmd=="remove":
        listt.remove(*args)
    elif cmd=="append":
        listt.append(*args)
    elif cmd=="sort":
        listt.sort()
    elif cmd=="pop":
        listt.pop()
    elif cmd=="reverse":
        listt.sort(reverse=True)                      
    
        
