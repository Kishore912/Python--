a=list(map(int,input().strip().split()))  #input() function reads a line of input from the user.
                                          #strip() method removes any leading or trailing whitespace characters from the input string.   
                                          #split() method splits the input string into a list of strings, using whitespace as the delimiter.
                                          #map() function applies the int() function to each element of the resulting list of strings, converting them into integers.
                                          #Finally, list() function converts the resulting map object into a list of integers.
print(a)   
max_of_number=0
for i in a:
    if i>max_of_number:
        max_of_number=i
print(max_of_number)                                                  

# finding a maximum number with out using max()