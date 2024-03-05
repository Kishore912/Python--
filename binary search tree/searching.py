class Node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.key=key

def insert(node,key):
    if node is None:
        return Node(key)
    else:
        if node.key<key :
            node.right=insert(node.right,key)
        else:
            node.left=insert(node.left,key)
    return node

def search(root,key):
    if root is None or root.key == key:
        return root
    if root.key<key:
        return search(root.right,key)
    return search(root.left,key)



r=Node(50)
r=insert(r,70)
r=insert(r,80)
r=insert(r,10)                    
r=insert(r,8)
r=insert(r,100)

key = 200
if search(r,key) is None:
    print(key,"not found")
else:
    print(key,"found")        


            