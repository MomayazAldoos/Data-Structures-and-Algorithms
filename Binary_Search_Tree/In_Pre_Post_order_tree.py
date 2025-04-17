def Inorder_tree_walk(x):
    if (x is not None):
        Inorder_tree_walk(x.left)
        print(x.value)
        Inorder_tree_wal(x.right)

def Preorder_tree_walk(x):
    if(x is not None):
        print(x.value)
        Preorder_tree_walk(x.left)
        Preorder_tree_walk(x.right)

def Post_tree_walk(x):
    if(x is not None):
        Post_tree_walk(x.left)
        Post_tree_walk(x.right)

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# Create nodes
root = Node(4)
root.left = Node(2)
root.right = Node(6)
root.left.left = Node(1)
root.left.right = Node(3)
root.right.left = Node(5)
root.right.right = Node(7)



#Inorder_tree_walk(root)
Preorder_tree_walk(root)
Inorder_tree_walk(root)
Post_tree_walk(root)