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
        if self.head is None:    # or  if self.length == 0
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

    def get(self,index):
        if index<0 or index>=self.length:
            return None
        
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp     


    def insert(self,index,value):
        if index<0 or index>=self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value) 
        
        newNode = Node(value)
        temp = self.get(index-1)
        newNode.next = temp.next
        temp.next = newNode
        self.length+=1
        return True


    def print_list(self):
        temp = self.head 
        while temp is not None:
            print(temp.value)
            temp = temp.next


my_linked_list = LinkedList(4)
my_linked_list.append(5)
my_linked_list.append(6)
my_linked_list.append(7)
my_linked_list.append(8)
my_linked_list.insert(1,15)
# print(my_linked_list.head.value)
# print(my_linked_list.tail.value)
# print(my_linked_list.length)
my_linked_list.print_list()
 