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

    def after_insert(self , prev_node , new_data):
        if prev_node is None:
            print("You must insert the previous node in LinkedList")
            return           
        
        new_node=Node(new_data)
        new_node.next=prev_node.next
        prev_node.next=new_node

    def print_it(self):
        current=self.head
        while current:
            print(current.data,end=" -> ")
            current=current.next
        print("None")        

my_linked_list=LinkedList()
my_linked_list.push(1)
my_linked_list.push(2)
my_linked_list.push(3)
my_linked_list.push(4)

print("LinkedList before insertion:")
my_linked_list.print_it()

prev_node_1 = my_linked_list.head.next
prev_node = prev_node_1.next
my_linked_list.after_insert(prev_node,7)

print("LinkedList after insertion:")
my_linked_list.print_it()