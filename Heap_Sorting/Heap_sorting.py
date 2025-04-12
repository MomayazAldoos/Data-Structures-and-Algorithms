def max_heapify(A, i, heap_size):
    # Calculate left child index (2*i + 1)
    left = 2 * i + 1
    # Calculate right child index (2*i + 2)
    right = 2 * i + 2
    # Assume the current node (i) is the largest
    largest = i
    
    # Compare left child with largest, if left exists and is greater
    if left < heap_size and A[left] > A[largest]:
        # Update largest to left child's index
        largest = left
    
    # Compare right child with largest, if right exists and is greater
    if right < heap_size and A[right] > A[largest]:
        # Update largest to right child's index
        largest = right
    
    # If largest is not the current node, swap and continue heapifying
    if largest != i:
        # Swap A[i] with A[largest]
        A[i], A[largest] = A[largest], A[i]
        # Recursively heapify the affected subtree
        max_heapify(A, largest, heap_size)

def build_max_heap(A):
    # Set heap_size to the full array length
    heap_size = len(A)
    # Start from the last non-leaf node (len(A)//2 - 1) to the root (0)
    for i in range(len(A)//2 - 1, -1, -1):
        # Apply max_heapify to ensure max-heap property
        max_heapify(A, i, heap_size)
    # Return heap_size for clarity (though modified in-place)
    return heap_size

def heap_sort(A):
    # Build a max-heap from the array
    heap_size = build_max_heap(A)
    # Iterate from the last element to the second element (index 1)
    for i in range(len(A)-1, 0, -1):
        # Swap root (maximum) with the last element of the heap
        A[0], A[i] = A[i], A[0]
        # Reduce heap size by 1 to exclude the sorted element
        heap_size -= 1
        # Restore max-heap property for the reduced heap
        max_heapify(A, 0, heap_size)
    # Array is now sorted in-place

    # Test function
def test_heap_sort():
    # Test case 1: Unsorted array
    arr1 = [64, 34, 25, 12, 22, 11, 90]
    print("Original array 1:", arr1)
    heap_sort(arr1)
    print("Sorted array 1:", arr1)
    
    # Test case 2: Already sorted array
    arr2 = [1, 2, 3, 4, 5]
    print("Original array 2:", arr2)
    heap_sort(arr2)
    print("Sorted array 2:", arr2)
    
    # Test case 3: Empty array
    arr3 = []
    print("Original array 3:", arr3)
    heap_sort(arr3)
    print("Sorted array 3:", arr3)
    
    # Test case 4: Single element
    arr4 = [42]
    print("Original array 4:", arr4)
    heap_sort(arr4)
    print("Sorted array 4:", arr4)
    
    # Test case 5: Array with duplicates
    arr5 = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    print("Original array 5:", arr5)
    heap_sort(arr5)
    print("Sorted array 5:", arr5)

if __name__ == "__main__":
    test_heap_sort()