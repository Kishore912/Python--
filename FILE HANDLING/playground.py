# creating a file hello.txt and writing in it 

f=open("hello.txt","w")
f.write("automatically the file get created and get writed")
f.close()

f=open("hello.txt","r")
print(f.read())
f.close()