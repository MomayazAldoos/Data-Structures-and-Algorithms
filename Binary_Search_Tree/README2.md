the searching in array is to determine if a given element (key) is in an array and in the affirmative case determine its position. 

we will study four typrs of searching trees:
1. Linear search
2. Binary search 
3. Jump search 
4. Exponential search 

First is Linear search :
Linear seach is ,also called sequential search, a method for finding an element(key) within an array. It sequentially checks each element of the array until a match is found or the whole array has been searched. 

The time-complexity:
- An unseccessful seach requires n key comparisons where all elements must be checked.
- a seuccessful search requires at most n key comparisions in the worst case.
- the time complexity is O(n)

- Binary search needs O(nlogn) time but we need to be done at once.
** The algorithm for binaey search:
Binary search(A,x,first,last) **NOTE** A is array, x is the element we looking for, first is the first element of the tree and last is the last one.
If (first > last) then return "A does not contain x "
mid = first + last / 2 
if A[mid ] = the return "A contains x on position med"
if A[mid ]> x then Binary search(A,x,first, mid-1)
Else Binary search(A,x,mid+1,last)
** the run time for Binary seaech: 
we know that the algorithm terminates once x = mid= n/2 
so the T(n) = T(n/2)+Θ(1)
and with master theorm a = 1, b =2 and d = 0 and since a = b^d so the run time is Θ(n^0logn) with base b which is Θ(logn)base two. 


Secondly Exponential Search:
Determine in exponentially growing steps a range in which the search key lust lie

Exponential Search(L,X) **NOTE** L is sorted array increasingly and x the element we looking efter.
If (x=L[1]) return 1 
i := 2 
While (x>L[i]) Do
    i := 2.i 
for(j=i/2+1, i)Do 
    if (L[i] = x) then return j 
return -1 

Time explicity is Θ(logx) with base two 


Tree search(x,k):
If x= NIL or x = k then return x
if (k < x.key) then tree seach(x.left, key)
else return tree search(x.right,k)

to find the minimum key in a binary search tree
Tree min(x):
while x.left is not NIL then x := x.left 
return x

find the max(x):
while x.right is not NIL DO
x= x.right
return x

** Insert tree(T,z):
x = T.root
y = NIL 
while (x is not NIL)Do 
y = x now x is the parent and we save its value in y to protect it
if z.key< x.key then x = x.left 
else x = x.right 

z.top = y 
if z.key < y.key then y.left = z
else y.right = z

we define the height of an empty tree as -1
AVL tree is a binary seach tree in which the height of two subtree rooted differ by at most 1









____________


