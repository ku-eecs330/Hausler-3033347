from random import randint, seed
import time

class Sorting:
    def __init__(self, size):
        self.arr = []  # Initialize an empty list
        self.size = size

    def add(self, element):
        if len(self.arr) < self.size:
            self.arr.append(element)
        else:
            print("Array is already full, cannot add more elements.")

    def selection_sort(self):
        n = len(self.arr)
        for i in range(n):
            min_index = i
            for j in range(i + 1, n):
                if self.arr[j] < self.arr[min_index]:
                    min_index = j
            self.arr[i], self.arr[min_index] = self.arr[min_index], self.arr[i]

    def max_heapify(self, n, i):
        largest = i
        left_child = 2 * i + 1
        right_child = 2 * i + 2

        if left_child < n and self.arr[left_child] > self.arr[largest]:
            largest = left_child

        if right_child < n and self.arr[right_child] > self.arr[largest]:
            largest = right_child

        if largest != i:
            self.arr[i], self.arr[largest] = self.arr[largest], self.arr[i]
            self.max_heapify(n, largest)

    def build_max_heap(self):
        n = len(self.arr)
        for i in range(n // 2 - 1, -1, -1):
            self.max_heapify(n, i)

    def heap_sort(self):
        n = len(self.arr)
        self.build_max_heap()
        for i in range(n - 1, 0, -1):
            self.arr[i], self.arr[0] = self.arr[0], self.arr[i]
            self.max_heapify(i, 0)

    def merge_sort(self):
        if len(self.arr) > 1:
            mid = len(self.arr) // 2
            left_half = self.arr[:mid]
            right_half = self.arr[mid:]

            left_sorting = Sorting(len(left_half))
            left_sorting.arr = left_half
            left_sorting.merge_sort()

            right_sorting = Sorting(len(right_half))
            right_sorting.arr = right_half
            right_sorting.merge_sort()

            i = j = k = 0

            while i < len(left_half) and j < len(right_half):
                if left_half[i] < right_half[j]:
                    self.arr[k] = left_half[i]
                    i += 1
                else:
                    self.arr[k] = right_half[j]
                    j += 1
                k += 1

            while i < len(left_half):
                self.arr[k] = left_half[i]
                i += 1
                k += 1

            while j < len(right_half):
                self.arr[k] = right_half[j]
                j += 1
                k += 1

    def test_sorting_time(self, sorting_method):
        start_time = time.time()

        if sorting_method == 'selection':
            self.selection_sort()
        elif sorting_method == 'heap':
            self.heap_sort()
        elif sorting_method == 'merge':
            self.merge_sort()

        end_time = time.time()
        return end_time - start_time

def is_sorted(arr):
    return arr == sorted(arr)

def test_sort_algorithms(sorting_method, set_seed=None):
    if set_seed is not None:
        seed(set_seed)
    
    sorting = Sorting(10)
    
    for _ in range(10):
        sorting.add(randint(1, 100))
    
    if sorting_method == 'selection':
        sorting.selection_sort()
        print("Selection Sort:", is_sorted(sorting.arr))
    elif sorting_method == 'heap':
        sorting.heap_sort()
        print("Heap Sort:", is_sorted(sorting.arr))
    elif sorting_method == 'merge':
        sorting.merge_sort()
        print("Merge Sort:", is_sorted(sorting.arr))

def run_time_tests():
    seeding = 45
    array_sizes = [10000, 20000, 30000, 40000, 50000]
    methods = ['selection', 'heap', 'merge']
    
    print("Array Size\tSelection Sort\t\tHeap Sort\t\tMerge Sort")
    
    for size in array_sizes:
        times = []
        
        for m in methods:
            sorting = Sorting(size)
            seed(seeding)
            
            for _ in range(size):
                sorting.add(randint(1, 50000))
            
            interval = sorting.test_sorting_time(m)
            times.append(interval)
        
        print(f"{size}\t\t{times[0]:.6f}\t\t{times[1]:.6f}\t\t{times[2]:.6f}")

# Test case execution
seed_num = 43
test_sort_algorithms('selection', seed_num)
test_sort_algorithms('heap', seed_num)
test_sort_algorithms('merge', seed_num)
run_time_tests()

# END OF CODE #


# Runtime complexity of each sorting algorithms:

    # Selection Sort: O(n^2) for the worst cases and also average cases
    # Performs poorly on large datasets because of its use of n^2
    # Worse than Heap and Merge Sort

    # Heap Sort: O(n log n) for the worst, average, and the best cases
    # It repeatedly extracts the maximum element after building a max heap
    # More effective than Selection Sort and equal to Merge Sort

    # Merge Sort: O(n log n) for the worst, average, and best cases
    # It divides the array into halves and then merges them back in a sorted order in the array
    # More effective than Selection Sort and equal to Heap Sort