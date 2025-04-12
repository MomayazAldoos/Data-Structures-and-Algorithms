### Heap Sort Algorithm

**Heap Sort** is another efficient sorting algorithm with a time complexity of **O(n log n)**, making it both fast and reliable for large datasets.

Heap Sort leverages a special tree-based data structure called a **binary heap**, which can be efficiently represented using an array. Specifically, it uses a **max-heap** which its runtime is O(log(n)), where for every node `i` (except the root), the following property holds:

> `A[parent(i)] ≥ A[i]`

This ensures that the largest element is always at the root of the heap.

---

### Steps in Heap Sort

1. **Build a Max Heap**:  
   First, we transform the input array into a **max-heap** using a helper function called `Build_Max_Heap`. This organizes the array into a tree structure where each parent node is greater than or equal to its children.

2. **Heapify**:  
   We use the `Max_Heapify` function to maintain the heap property during sorting. This function ensures that the subtree rooted at a given index satisfies the max-heap condition.

3. **Heap Sort**:  
   Finally, the `Heap_Sort` function sorts the array. It repeatedly extracts the maximum element from the heap and places it at the end of the array, reducing the heap size each time and reapplying `Max_Heapify`.

