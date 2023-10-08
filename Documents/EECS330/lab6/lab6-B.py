class TreeNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

class TreeMap:
    def __init__(self):
        self.root = None

    def put(self, key, value):
        self.root = self.put_rec(self.root, key, value)

    def put_rec(self, node, key, value):
        if node is None:
            return TreeNode(key, value)
        if key < node.key:
            node.left = self.put_rec(node.left, key, value)
        elif key > node.key:
            node.right = self.put_rec(node.right, key, value)
        else:
            node.value = value
        return node

    def get(self, key):
        return self.get_rec(self.root, key)

    def get_rec(self, node, key):
        if node is None:
            return None
        if key == node.key:
            return node.value
        elif key < node.key:
            return self.get_rec(node.left, key)
        else:
            return self.get_rec(node.right, key)
        
tree_map = TreeMap()

# Test putting and getting key-value pairs.
tree_map.put(3, "A")
tree_map.put(1, "B")
tree_map.put(2, "C")
tree_map.put(4, "D")

assert tree_map.get(2) == "C"
assert tree_map.get(1) == "B"
assert tree_map.get(4) == "D"
# Non-existent key should return None.
assert tree_map.get(5) is None
