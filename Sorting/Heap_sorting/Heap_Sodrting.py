def heap_sort(A):
    # Adjust for 1-based indexing: insert a dummy element at index 0
    A.insert(0, None)  # A becomes [None, 4, 2, 6]
    
    def build_max_heap(A):
        n = len(A) - 1  # Effective length (1-based indices: 1 to n)
        for i in range(n // 2, 0, -1):  # From floor(n/2) down to 1
            max_heapify(A, i)
    
    def max_heapify(A, i):
        left = 2 * i
        right = 2 * i + 1
        largest = i
        if left <= len(A) - 1 and A[left] > A[largest]:
            largest = left
        if right <= len(A) - 1 and A[right] > A[largest]:
            largest = right
        if largest != i:
            A[i], A[largest] = A[largest], A[i]  # Swap
            max_heapify(A, largest)
    
    # Step 1: Build the max-heap
    build_max_heap(A)
    
    # Step 2: Extract elements from the heap
    for i in range(len(A) - 1, 1, -1):  # From n down to 2
        A[1], A[i] = A[i], A[1]  # Swap root (max) with the last element
        max_heapify(A, 1)  # Restore heap property (heap size decreases)
    
    # Remove the dummy element and return the sorted array
    A.pop(0)  # Remove index 0
    return A

# Test the function
A = [4, 2, 6]
sorted_A = heap_sort(A)
print(sorted_A)  # Output: [2, 4, 6]