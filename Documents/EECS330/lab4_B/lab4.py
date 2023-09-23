class Node:
    def __init__(self, data):
        self.item = data
        self.next = None
        self.prev = None

class Deque:
    def __init__(self):
        self.front_node = None
        self.back_node = None
        self.size = 0
    
    def is_empty(self):
        return self.size == 0

    def get_size(self) -> int:
        return self.size

    def push_front(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.front_node = self.back_node = new_node
        else:
            new_node.next = self.front_node
            self.front_node.prev = new_node
            self.front_node = new_node
        self.size += 1

    def push(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.front_node = self.back_node = new_node
        else:
            new_node.prev = self.back_node
            self.back_node.next = new_node
            self.back_node = new_node
        self.size += 1

    def pop_front(self) -> int:
        if self.is_empty():
            raise Exception("Deque is empty. Cannot pop from front.")
        if self.size == 1:
            popped_item = self.front_node.item
            self.front_node = self.back_node = None
        else:
            popped_item = self.front_node.item
            self.front_node = self.front_node.next 
            self.front_node.prev = None
        self.size -= 1
        return popped_item
    
    def pop_back(self) -> int:
        if self.is_empty():
            raise Exception("Deque is empty. Cannot pop from back.")
        if self.size == 1:
            popped_item = self.back_node.item
            self.back_node = self.front_node = None
        else:
            popped_item = self.back_node.item
            self.back_node = self.back_node.prev
            self.back_node.next = None
        self.size -= 1
        return popped_item
    
    def get_front_item(self) -> int:
        if self.is_empty():
            raise IndexError("Deque is empty, cannot access the front.")
        return self.front_node.item
    
    def get_back_item(self) -> int:
        if self.is_empty():
            raise IndexError("Deque is empty, cannot access the back.")
        return self.back_node.item

