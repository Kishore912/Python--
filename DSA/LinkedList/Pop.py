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

    def pop(self):
        if self.head is None:
            return None
        pre = self.head
        temp = self.head
        while temp.next is not None:    #  or while (temp.next):
            pre = temp
            temp = temp.next     
        self.tail = pre
        self.tail.next = None 
        self.length -=1  
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp.value
       
             

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next



my_linked_list = LinkedList(1)
my_linked_list.append(2)
# my_linked_list.append(3)
# my_linked_list.print_list()     
print(my_linked_list.pop()) 
print(my_linked_list.pop())
print(my_linked_list.pop())