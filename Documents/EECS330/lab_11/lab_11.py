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

    def quicksort(self, low, high):
        if low < high:
            pi = self.partition(low, high)  # Partitioning index
            self.quicksort(low, pi-1)  # Recursively sort elements before partition
            self.quicksort(pi+1, high)  # Recursively sort elements after partition

    def partition(self, low, high):
        pivot_index = self.median_of_three(low, high)
        pivot_value = self.arr[pivot_index]

        # Swap pivot with the last element
        self.arr[pivot_index], self.arr[high] = self.arr[high], self.arr[pivot_index]

        i = low - 1
        for j in range(low, high):
            if self.arr[j] <= pivot_value:
                i += 1
                # Swap elements at i and j
                self.arr[i], self.arr[j] = self.arr[j], self.arr[i]

        # Swap pivot back to its final position
        self.arr[i + 1], self.arr[high] = self.arr[high], self.arr[i + 1]
        return i + 1

    def median_of_three(self, low, high):
        mid = (low + high) // 2
        candidates = [(low, self.arr[low]), (mid, self.arr[mid]), (high, self.arr[high])]
        # Sort the candidates based on values
        candidates.sort(key=lambda x: x[1])
        return candidates[1][0]

    @staticmethod
    def counting_sort(arr, exp):
        n = len(arr)

        # Initialize count array and output array
        count = [0] * 10
        output = [0] * n

        # Count occurrences of each digit
        for i in range(n):
            index = arr[i] // exp
            count[index % 10] += 1

        # Update count to store the position of the next occurrence
        for i in range(1, 10):
            count[i] += count[i - 1]

        # Build the output array
        i = n - 1
        while i >= 0:
            index = arr[i] // exp
            output[count[index % 10] - 1] = arr[i]
            count[index % 10] -= 1
            i -= 1

        # Copy the output array to the original array
        for i in range(n):
            arr[i] = output[i]

    @staticmethod
    def radix_sort(arr):
        # Return if array is empty
        if len(arr) == 0:
            return

        # Find the maximum number to know the number of digits
        max_num = max(arr)

        # Do counting sort for every digit
        exp = 1
        while max_num // exp > 0:
            Sorting.counting_sort(arr, exp)
            exp *= 10


# Test quick sorting technique
def is_sorted(arr):
    if arr == sorted(arr):
        return "Passed!"
    else:
        return "Failed!"

def test_quicksort():
    """Test the Quicksort algorithm"""
    seed_num = 43
    seed(seed_num)  # Set the seed for reproducibility
    sorting = Sorting(10)
    for _ in range(10):
        sorting.add(randint(1, 100))

    sorting.quicksort(0, len(sorting.arr) - 1)  # Apply the Quicksort algorithm
    print("Quick Sort:", is_sorted(sorting.arr))

# Test case execution
test_quicksort()

# Test radix sorting technique
def test_radix_sort():
    # Test case 1
    sorting = Sorting(8)
    arr1 = [234, 34, 34, 2, 1, 0, 2, 3422]
    sorting.radix_sort(arr1)
    assert arr1 == [0, 1, 2, 2, 34, 34, 234, 3422], f"Test case 1 failed: {arr1}"

    # Test case 2
    sorting = Sorting(7)
    arr2 = [329, 457, 657, 839, 436, 720, 355]
    sorting.radix_sort(arr2)
    assert arr2 == [329, 355, 436, 457, 657, 720, 839], f"Test case 2 failed: {arr2}"

    # Test case 3
    sorting = Sorting(5)
    arr3 = [1, 200, 3, 400, 5]
    sorting.radix_sort(arr3)
    assert arr3 == [1, 3, 5, 200, 400], f"Test case 3 failed: {arr3}"

    # Test case 4 (empty array)
    sorting = Sorting(0)
    arr4 = []
    sorting.radix_sort(arr4)
    assert arr4 == [], f"Test case 4 failed: {arr4}"

    # Test case 5 (array with one element)
    sorting = Sorting(1)
    arr5 = [42]
    sorting.radix_sort(arr5)
    assert arr5 == [42], f"Test case 5 failed: {arr5}"

    print("All test cases passed!")

# Run the test cases
test_radix_sort()

