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

    def get(self,index):
        if index<0 or index>=self.length:
            return None
        
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp  

    def set(self,index,value):
        temp = self.get(index)                     # if index<0 or index>=self.length:
        if temp:                                        # return None
            temp.value = value                     # temp = self.head
            return True                            # for _ in range(index):
        return False     
       
             

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next


    def remove(self,index):
        if index<0 or index>=self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length-1:
            return self.pop()
        prev = self.get(index-1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp
    

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        After = temp.next
        before = None
        for _ in range(self.length):
            After = temp.next
            temp.next = before
            before = temp
            temp = After

myLinkedList = LinkedList(11)
myLinkedList.append(3)
myLinkedList.append(2)
myLinkedList.append(21)
myLinkedList.reverse()
myLinkedList.print_list()   
