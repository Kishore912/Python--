class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def push(self,new_data):
        new_node=Node(new_data)
        new_node.next=self.head
        self.head=new_node

    def print_it(self):
        current=self.head
        while current:
            print(current.data , end=" -> ")
            current=current.next
        print("None")


my_linked_list=LinkedList()
my_linked_list.push(6)
my_linked_list.push(4)
my_linked_list.push(3)
my_linked_list.push(1)

print("LinkedList: ")
my_linked_list.print_it()                                    