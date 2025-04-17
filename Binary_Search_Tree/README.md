
A binary tree is rooted tree for each vertex has almost two children. However each vertex x is an object with:
    x.key which is a value to be sorted
    x.top which is the parent of x 
    x.left is the left child 
    x.right is the right child 
In case a child or the parent is missing, then the appropriate attribute contains the value NIL.

The binary search tree is a binary tree in which the keys are always sorted a way: 
   -y is a node in the left subtree of x, then y.key <= x.key 
   -y is a node in the right subtree of x, then y.key >= x.key 

which means in other words that the last element to the left is the minimum element and the last right element is the biggest one. 

We have too the traversing in the binary search tree:
1. Preorder:
    - visit the current vertex
    - recursively traverse left subtree 
    - recursively traverse right subtree.

2. Postorder:
    - recursively traverse left vertex
    - recursively traverse right vertex.
    - visit current vertex.
3. Inorder:
    - recursively traverse left subtree
    - visit current vertex
    - recursively traverse right subtree

______

I will take advatages of BST for att generate an algorithm that can find a spicific element in any where of the tree which is the maximum or the minimum element. and the runtime of such an algorithm is O(n) which is fast and perfect. 

____
Then i will generate an inseration tree which takes a BST and an element as arguments. which takes O(h) as runtime and h here is the height of the binary search tree. This function help us add anyb element to the tree in the right place based on some conditions whether this place is the right one or should we move to the left or right place or even add it to the root directly. 

______
NOTE: the height of an empty tree is -1 
We went deep to AVL tree which is a balanced tree that the difference between tw subtree height rooted of any vertex is almost 1 {1,0,-1}
and the thing that we know about AVL tree is that the runtime for it is O(nlogn)´

