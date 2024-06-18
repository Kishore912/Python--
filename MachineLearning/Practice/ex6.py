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

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def pop(self):
        if self.head is None:
            return None
        pre = self.head
        temp = self.head
        while temp.next is not None:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length-=1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp.value    

myLinkedList = LinkedList(4)
myLinkedList.append(5)
myLinkedList.append(6)
myLinkedList.print_list()
# print(myLinkedList.pop())
# print(myLinkedList.pop())
# print(myLinkedList.pop())

    