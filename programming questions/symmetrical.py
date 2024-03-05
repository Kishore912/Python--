def symmetrical(word):
    n=len(word) #6
    if n%2:
      mid = n//2+1    
    else:
       mid = n//2 #3

    start=0
    flag=0
    end=mid #3

    while(start<mid and end<n):
        if(word[start]==word[end]):
          start+=1
          end+=1
        else:
          flag=1
          break  
    if flag==0:
       print("the given word is symmetrical")
    else:
       print("the given word is not symmetrical")       
       
    
symmetrical(input())    