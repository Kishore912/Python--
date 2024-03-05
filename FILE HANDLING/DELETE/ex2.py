import os
if os.path.exists("hello.txt"):
    os.remove("hello.txt")
else:
    print("file does'nt exists")    