from collections import deque

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
        self._node_count = 0  

    def size(self):
        return self._node_count

    def insert(self, key):
        new_node = TreeNode(key)
        if not self.root:
            self.root = new_node
        else:
            self.insert_rec(self.root, new_node)
        self._node_count += 1

    def insert_rec(self, current_node, new_node):
        if new_node.value <= current_node.value:
            if current_node.left is None:
                current_node.left = new_node
            else:
                self.insert_rec(current_node.left, new_node)
        else:
            if current_node.right is None:
                current_node.right = new_node
            else:
                self.insert_rec(current_node.right, new_node)

    def search(self, key) -> TreeNode:
        return self.search_rec(self.root, key)

    def search_rec(self, current_node, key):
        if current_node is None:
            return None
        if current_node.value == key:
            return current_node
        left_result = self.search_rec(current_node.left, key)
        if left_result:
            return left_result  
        return self.search_rec(current_node.right, key)
    
    def level_order_traversal(self) -> list:
        result = []
        if not self.root:
            return result
        queue = deque()
        queue.append(self.root)

        while queue:
            current_node = queue.popleft()
            result.append(current_node.value)
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
        return result

# Initialize BST.
bst = BinarySearchTree()

# Test inserting nodes
bst.insert(5)
bst.insert(3)
bst.insert(8)
bst.insert(2)
bst.insert(4)
bst.insert(7)
bst.insert(9)

# Test size method.
assert bst.size() == 7
assert bst.search(1) == None

# Test inserting additional nodes.
bst.insert(1)
bst.insert(6)

assert bst.size() == 9
assert bst.search(1).value == 1

# Finally, also test by inserting duplicate values.

# Test level order traversal with duplicates.
bst = BinarySearchTree()
bst.insert(5)
bst.insert(3)
bst.insert(8)
bst.insert(2)
bst.insert(4)
bst.insert(7)
bst.insert(9)
bst.insert(5)
bst.insert(7)
bst.insert(1)
bst.insert(6)
bst.insert(1)
bst.insert(6)

# Test level order traversal.
assert bst.level_order_traversal() == [5, 3, 8, 2, 4, 7, 9, 1, 5, 7, 1, 6, 6]
