class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self,value):
        newNode = Node(value)
        self.top = newNode
        self.height = 1

    def print_stack(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def push(self,value):
        newNode  = Node(value)
        if self.height == 0:
            self.top = newNode
        else:
            newNode.next = self.top
            self.top = newNode
        self.height += 1        

My_Stack = Stack(4)
My_Stack.push(5)
My_Stack.push(6)
My_Stack.print_stack()                


    