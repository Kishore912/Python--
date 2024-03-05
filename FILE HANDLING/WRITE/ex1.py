f=open("blank.txt","a")
f.write("\na new line is appended")
f.close()
f=open("blank.txt","r")
print(f.read())
f.close()

#-------------------------------------------------------------------------------------------

z=open("blank.txt","w")
z.write("i have overwrited the contents")
z.close()

z=open("blank.txt","r")
print(z.read())
z.close()

#-----------------------------------------------------------------------------------------------

# x=open("empty.txt","x")

#------------------------------------------------------------------------------------------------