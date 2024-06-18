class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self,value):
        newNode = Node(value)
        self.head = newNode
        self.tail = newNode
        self.length = 1

    def append(self,value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
        self.length+=1
    
    def prepend(self,value):
        newNode = Node(value)
        if self.head is None:      # or  if self.length == 0:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head 
            self.head = newNode
        self.length+=1
        return True    

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

mylinkedlist = LinkedList(2)
mylinkedlist.append(3)
mylinkedlist.append(4)

mylinkedlist.prepend(1)
mylinkedlist.print_list()
                                        