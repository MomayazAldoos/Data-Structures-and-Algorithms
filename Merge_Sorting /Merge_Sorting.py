def merge(A, p, q, r):
    n1 = q - p + 1 #length of the lesft subarray 
    n2 = r - q     #length of the right subarray
    
    # Create  temporary arrays L and R
    L = [0] * (n1 + 1)
    R = [0] * (n2 + 1)

    # Copy data to temporary arrays 
    for i in range(n1):
        L[i] = A[p + i]
    for j in range(n2):
        R[j] = A[q + j + 1]

    # Add sentinel values (infinity) to avoid index bounds checking 
    L[n1] = float('inf')
    R[n2] = float('inf')
    i = 0
    j = 0
    k = p
    while k <= r:
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1

def merge_sort(A, p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort(A, p, q) # Sort left half
        merge_sort(A, q + 1, r) # Sort right half 
        merge(A, p, q, r) # Merge the sorted halves

# Test function
def test_merge_sort():
    # Test case 1: Unsorted array
    arr1 = [64, 34, 25, 12, 22, 11, 90]
    print("Original array 1:", arr1)
    merge_sort(arr1, 0, len(arr1)-1)
    print("Sorted array 1:", arr1)
    
    # Test case 2: Already sorted array
    arr2 = [1, 2, 3, 4, 5]
    print("Original array 2:", arr2)
    merge_sort(arr2, 0, len(arr2)-1)
    print("Sorted array 2:", arr2)
    
    # Test case 3: Empty array
    arr3 = []
    print("Original array 3:", arr3)
    if len(arr3) > 0:
        merge_sort(arr3, 0, len(arr3)-1)
    print("Sorted array 3:", arr3)
    
    # Test case 4: Single element
    arr4 = [42]
    print("Original array 4:", arr4)
    merge_sort(arr4, 0, len(arr4)-1)
    print("Sorted array 4:", arr4)
    
    # Test case 5: Array with duplicates
    arr5 = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    print("Original array 5:", arr5)
    merge_sort(arr5, 0, len(arr5)-1)
    print("Sorted array 5:", arr5)

if __name__ == "__main__":
    test_merge_sort()


