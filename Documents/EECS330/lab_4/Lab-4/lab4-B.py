class Node:
    def __init__(self, data):
        self.item = data
        self.next = None
        self.prev = None

class Deque:
    def __init__(self):
        self.front = None
        self.back = None
        self.size = 0
    
    def empty(self):
        if self.size == 0:
            return True
        else:
            return False

    def get_size(self) -> int:
        return self.size

    def push_front(self, data):
        new_node = Node(data)
        if self.empty():
            self.front = self.back = new_node
        else:
            new_node.next = self.front
            self.front.prev = new_node
            self.front = new_node
        self.size += 1

    def push(self, data):
        new_node = Node(data)
        if self.empty():
            self.front = self.back = new_node
        else:
            new_node.prev = self.back
            self.back.next = new_node
            self.back = new_node
        self.size += 1

    def pop_front(self) -> int:
        if self.empty():
            raise Exception("Deque is empty. Cannot pop from front.")
        if self.size == 1:
            popped_item = self.front.item
            self.front = self.back = None
        else:
            popped_item = self.front.item
            self.front = self.front.next 
            self.front.prev = None
        self.size -= 1
        return popped_item
    
    def pop(self) -> int:
        if self.empty():
            raise Exception("Deque is empty. Cannot pop from back.")
        if self.size == 1:
            popped_item = self.front.item
            self.back = self.front = None
        else:
            popped_item = self.back.item
            self.back = self.back.prev
            self.back.next = None
        self.size -= 1
        return popped_item
    
    def front(self) -> int:
        if self.size == 0:
            raise IndexError("Deque is empty, cannot access the front index.")
        return self.front.item
    
    def back(self) -> int:
        if self.size == 0:
            raise IndexError("Deque is empty, cannot access the back index.")
        return self.back.item      