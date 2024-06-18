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

    def pop_first(self):
        if self.head is None:
            return None
        
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length-=1

        if self.length == 0:
            self.tail = None
        return temp.value    
                
       
             

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next



my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
     
print(my_linked_list.pop_first()) 

