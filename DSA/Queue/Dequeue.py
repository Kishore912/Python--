class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self,value):
        newNode = Node(value)
        self.first = newNode
        self.last = newNode
        self.length = 1

    def Enqueue(self,value):
        newNode = Node(value)
        if self.length == 0:
            self.first = newNode
            self.last = newNode
        else:
            self.last.next = newNode
            self.last = newNode
        self.length += 1              

    def Dequeue(self):
        if self.length == 0:
            return None
        temp = self.first
        if self.length == 1:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next
            temp.next = None
        self.length -= 1
        return temp.value                      

    def print_queue(self):
        temp = self.first
        while temp is not None:
            print(temp.value)
            temp = temp.next
            

my_Queue = Queue(1)
my_Queue.Enqueue(2)
my_Queue.Enqueue(3)   
print(my_Queue.Dequeue(),'\n')     
my_Queue.print_queue()