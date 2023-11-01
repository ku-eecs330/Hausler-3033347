import numpy as np


class Deque:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.front = -1
        self.back = -1
        self.size = 0
        self.array = np.empty(self.capacity, dtype=object)

    def is_empty(self):
        return self.size == 0

    def get_size(self):
        return self.size

    def push_front(self, data):
        if self.is_empty():
            self.front = self.back = 0
        else:
            self.front = (self.front - 1) % self.capacity
        self.array[self.front] = str(data)  # Convert data to a string
        self.size += 1

    def push(self, data):
        if self.is_empty():
            self.front = self.back = 0
        else:
            self.back = (self.back + 1) % self.capacity
        self.array[self.back] = str(data)  # Convert data to a string
        self.size += 1

    def pop_front(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        data = self.array[self.front]
        if self.front == self.back:
            self.front = self.back = -1
        else:
            self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return data

    def pop(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        data = self.array[self.back]
        if self.front == self.back:
            self.front = self.back = -1
        else:
            self.back = (self.back - 1) % self.capacity
        self.size -= 1
        return data

    def resize(self):
        new_capacity = self.capacity * 2
        new_array = np.empty(new_capacity, dtype=object)
        if not self.is_empty():
            i = self.front
            j = 0
            while True:
                new_array[j] = self.array[i]
                j += 1
                if i == self.back:
                    break
                i = (i + 1) % self.capacity
        self.front = 0
        self.back = self.size - 1
        self.capacity = new_capacity
        self.array = new_array

    @staticmethod
    def reverse_deque(deque):
        reversed_deque = Deque()
        while not deque.is_empty():
            reversed_deque.push(deque.pop_front())
        return reversed_deque


def isPalindrome(s: str) -> bool:
    s = ''.join(filter(str.isalnum, s)).lower()
    deque = Deque()
    for char in s:
        deque.push(char)
    while deque.get_size() > 1:
        front_char = deque.pop_front()
        back_char = deque.pop()
        if front_char != back_char:
            return False
    return True


print("Reverse Method:")
deque = Deque()
deque.push(1)
deque.push(2)
deque.push(3)

reversed_deque = Deque.reverse_deque(deque)
while not reversed_deque.is_empty():
    print(reversed_deque.pop())

print("\nPalindrome Method:")
test1 = "racecar"
test2 = "hello"
print(isPalindrome(test1))  # True
print(isPalindrome(test2))  # False


