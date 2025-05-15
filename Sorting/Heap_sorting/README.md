# HeapSort Implementation in Python

## Overview
This repository contains a Python implementation of the **HeapSort** algorithm, a comparison-based sorting technique with a time complexity of O(n log n). The implementation leverages a max-heap data structure, utilizing two nested functions: `build_max_heap` to construct the heap and `max_heapify` to maintain the heap property. The code is designed with 1-based indexing for clarity in the heap structure, using a dummy element at index 0 to simulate this convention in Python's 0-based array system.

## Features
- In-place sorting algorithm with O(n log n) time complexity.
- Nested functions for modular design: `build_max_heap` and `max_heapify`.
- Tested with example input `[4, 2, 6]`, producing the sorted output `[2, 4, 6]`.
- Well-commented code for readability and educational purposes.

## Code Structure
- **File**: `heap_sort.py`
  - Contains the main `heap_sort` function with nested `build_max_heap` and `max_heapify` functions.
  - Uses a dummy element at index 0 to support 1-based indexing for heap operations.

## How It Works
1. **Heap Construction**: The `build_max_heap` function transforms the input array into a max-heap by iterating from the last non-leaf node (at \( \lfloor n/2 \rfloor \)) down to the root, calling `max_heapify` on each node.
2. **Heap Sorting**: The `heap_sort` function repeatedly extracts the maximum element (root of the max-heap) and places it at the end of the array, reducing the heap size and restoring the heap property with `max_heapify`.
3. **Output**: Returns the sorted array in ascending order after removing the dummy element.
