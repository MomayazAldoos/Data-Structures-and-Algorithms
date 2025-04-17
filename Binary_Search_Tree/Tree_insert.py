class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.top = None

def tree_insert(t, z):
    x = t  # Start at the root node
    y = None  # Parent of the new node
    while x is not None:
        y = x  # Save the current node as parent
        if z.value < x.value:
            x = x.left
        else:
            x = x.right
    z.top = y  # Set the parent of z
    if y is None:  # If tree was empty
        return z  # z becomes the new root
    if z.value < y.value:
        y.left = z
    else:
        y.right = z
    return t  # Return the tree

# Function to print the tree (inorder traversal for sorted order)
def print_inorder(node):
    if node:
        print_inorder(node.left)
        print(node.value, end=" ")
        print_inorder(node.right)

# Create the tree
root = Node(4)
root.left = Node(2)
root.right = Node(6)
root.left.left = Node(1)
root.left.right = Node(3)
root.right.left = Node(5)
root.right.right = Node(7)

# Print tree before insertion
print("Tree before insertion:", end=" ")
print_inorder(root)  # Should print: 1 2 3 4 5 6 7
print()

# Insert a new node with value 10
z = Node(10)
root = tree_insert(root, z)

# Print tree after insertion
print("Tree after insertion of 10:", end=" ")
print_inorder(root)  # Should print: 1 2 3 4 5 6 7 10
print()