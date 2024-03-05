x=lambda a:a*10
print(x(10))

#---------------------------

def Func(b):
    return lambda a:a*b
result=Func(10)
print(result(2))
print(result(5))