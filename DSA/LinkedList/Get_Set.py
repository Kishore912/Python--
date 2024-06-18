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

    def get(self,index):
        if index<0 or index>=self.length:
            return None
        
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp        # return temp.value    to get the value    


    def set(self,index,value):
        temp = self.get(index)                     # if index<0 or index>=self.length:
        if temp:                                        # return None
            temp.value = value                     # temp = self.head
            return True                            # for _ in range(index):
        return False                                    # temp = temp.next
                                                        # temp.value = value
                                                   # return temp.value    
    def print_list(self):
        temp = self.head 
        while temp is not None:
            print(temp.value)
            temp = temp.next


my_linked_list = LinkedList(0)
my_linked_list.append(1)
my_linked_list.append(2)
my_linked_list.append(3)

# print(my_linked_list.get(1))
my_linked_list.set(2,10)
my_linked_list.print_list()
 