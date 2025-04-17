def tree_search(x, k):
    if(x is None or k==x.key):
        return x
    if( k<x.key):
        return tree_search(x.left, k)
    else:
        return tree_search(x.right, k)


# Create a function that find the min element in BST:

def find_min(t):
    if t is  None:
        return ("Minimum element here is noll")
    if t.left is  None:
        return t.key
    return find_min(t.left)

# Create a function that find the max element in BST:
def find_max(t):
    if t is  None:
        return ("max element here is noll")
    if t.right is  None:
        return t.key
    return find_max(t.right)

class Node:
    def __init__(self, key):
        self.key = key
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

key = 2
key2 = 68
result = tree_search(root, key)
result2 = tree_search(root, key2)

if result:
    print(f"Hittade värde {result.key}")
else:
    print("Not in the tree")

if result2:
    print(f"Hittade värde {result2.key}")
else:
    print("Not in the tree")

print(find_max(root))
print(find_min(root))

