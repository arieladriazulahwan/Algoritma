import time

# Bubble sort implementation
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Quick sort implementation
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Input arrays
a = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
b = [0, 1, 2, 3, 4, 9, 8, 7, 6, 5]

# Measure time for Bubble Sort and Quick Sort on both arrays
for label, array in [("a", a), ("b", b)]:
    print(f"Sorting array {label}: {array}")
    
    # Bubble sort timing
    array_bubble = array[:]
    start = time.time()
    bubble_sort(array_bubble)
    bubble_time = time.time() - start
    print(f"Bubble Sort result: {array_bubble}, Time: {bubble_time:.6f} seconds")
    
    # Quick sort timing
    array_quick = array[:]
    start = time.time()
    quick_sorted = quick_sort(array_quick)
    quick_time = time.time() - start
    print(f"Quick Sort result: {quick_sorted}, Time: {quick_time:.6f} seconds")
    print()
    
 # Hasil Analisis :
 #Quick Sort lebih efektif untuk kedua kasus, terutama jika array menjadi lebih besar. 