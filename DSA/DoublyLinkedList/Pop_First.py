class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self,value):
        newNode = Node(value)
        self.head = newNode
        self.tail = newNode
        self.length = 1

    def append(self,value):
        newNode = Node(value)
        if self.length == 0:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode
        self.length+=1
        return True

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next


    def Pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            temp = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None        
        self.length -= 1  
        return temp

    def Prepend(self,value):
        newNode = Node(value)
        if self.length == 0:
            self.head = None
            self.tail = None
        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
        self.length+=1
        return True        

    def Pop_First(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            temp.next = None
            self.head.prev = None 
        self.length-=1
        return temp.value

    
    


myDoublyLinkedList  = DoublyLinkedList(1)
myDoublyLinkedList.append(2)
myDoublyLinkedList.append(3)
myDoublyLinkedList.Pop_First()

myDoublyLinkedList.print_list()          
    
