class Node:
    def __init__(self,value):
        self.value = value              # this class constructor will create a new node with a value and a next pointer with none
        self.next = None

class LinkedList:
    def __init__(self,value):
        newNode = Node(value)          # In this line we are calling that new node 
        self.head = newNode            # Pointing the head pointer to the created new node
        self.tail = newNode            # pointing the tail pointer to the created new node
        self.length = 1

my_LinkedList = LinkedList(4)
print(my_LinkedList.head.value)           