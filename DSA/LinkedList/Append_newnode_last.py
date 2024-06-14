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

    def print_list(self):
        temp = self.head 
        while temp is not None:
            print(temp.value)
            temp = temp.next


my_linked_list = LinkedList(4)
my_linked_list.append(5)
my_linked_list.append(6)

# print(my_linked_list.head.value)
# print(my_linked_list.tail.value)
# print(my_linked_list.length)
print(my_linked_list.print_list())
 