from art import logo
import os
def add(n1,n2):
  return n1+n2

def subtract(n1,n2):
  return n1 - n2

def multiply(n1,n2):
  return n1 * n2

def divide(n1,n2):
  return n1 / n2

operations={
  "+" : add ,
  "-" : subtract ,
  "*" : multiply ,
  "/" : divide
}

def calculator():
  print(logo)
  num1=float(input("What is the first number : "))
  for symbols in operations:
    print(symbols)
    
  x=True
  while x:
    num2=float(input("What is the next number : "))
    operation_symbol=input("pic a operation  ")
    function=operations[operation_symbol]
    answer=function(num1,num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    
    if input(f"Type 'y' to continue with {answer} or 'n' to start a new calculation ")=="y":
      num1=answer
    else:
      
      x=False
      os.system('cls')
      calculator()
      
  
calculator()  
