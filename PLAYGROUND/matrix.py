# first we declaring a matrix like this 

row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"] 
# and then nesting all the list in a map which makes it a nested list
map = [row1, row2, row3]
#printing all the list in a line which makes it looks like a matrix
print(f"{row1}\n{row2}\n{row3}")
#get the column and row from the user
position = input("Where do you want to put the treasure? ")

horizontal=int(position[0]) #2           #here we taking the first integer as horizontal
vertical=int(position[1])  #3            #here we taking the second integer as vertical
v=map[vertical-1]   #3-1=2 in map is row 3
v[horizontal-1]="X"  #now row3 of 2-1=1st index is changed as "X"


print(f"{row1}\n{row2}\n{row3}")

