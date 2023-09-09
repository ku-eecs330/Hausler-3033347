class SLList:
    class IntNode:
        def __init__(self, item, next_node):
            self.item = item  # int
            self.next = next_node  # IntNode

    def __init__(self):
        self.first = None  # initialize an empty list

    def addFirst(self, item):
        self.first = self.IntNode(item, self.first)

    def insert(self, item, position):
        if position < 0:
            return ValueError("Position must be a non-negative integer")
        if position == 0:
            self.addFirst(item)
            return
        current = self.first
        index = 0
        while current is not None and index < position - 1:
            current = current.next
            index += 1
        if current is None:
            raise IndexError("Position is out of range")
        new_node = self.IntNode(item, current.next)
        current.next = new_node
        
    def reverse(self):
        prev = None
        current = self.first
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.first = prev
        
    def replicate(self, count):
        if count <= 0:
            return
        current = self.first
        while current is not None:
            for _ in range(count - 1):
                new_node = self.IntNode(current.item, current.next)
                current.next = new_node
                current = new_node
            current = current.next
        
    def __str__(self):
        result = []
        current = self.first
        while current:
            result.append(str(current.item))
            current = current.next
        return " -> ".join(result)
    
    def equals(self, anotherList):
        current1 = self.first
        current2 = anotherList.first
        while current1 is not None and current2 is not None:
            if current1.item != current2.item:
                return False
            current1 = current1.next
            current2 = current2.next
        return current1 is None and current2 is None
    
if __name__ == '__main__':
  L = SLList()
  L.addFirst(15)
  L.addFirst(10)
  L.addFirst(5)
  L.reverse()

  L_expect = SLList()
  L_expect.addFirst(5)
  L_expect.addFirst(10)
  L_expect.addFirst(15)	

  if L.equals(L_expect):
    print("Two lists are equal, tests passed")
  else:
    print("Two lists are not equal, tests failed")

