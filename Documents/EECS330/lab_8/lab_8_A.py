class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def preorder_traversal(self) -> list:
        result = []
        self._preorder_recursive(self.root, result)
        return result

    def _preorder_recursive(self, current_node, result):
        if current_node:
            result.append(current_node.value)
            self._preorder_recursive(current_node.left, result)
            self._preorder_recursive(current_node.right, result)

    def inorder_traversal(self) -> list:
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, current_node, result):
        if current_node:
            self._inorder_recursive(current_node.left, result)
            result.append(current_node.value)
            self._inorder_recursive(current_node.right, result)

    def postorder_traversal(self) -> list:
        result = []
        self._postorder_recursive(self.root, result)
        return result

    def _postorder_recursive(self, current_node, result):
        if current_node:
            self._postorder_recursive(current_node.left, result)
            self._postorder_recursive(current_node.right, result)
            result.append(current_node.value)

# Create a binary tree
bt = BinaryTree()
bt.root = TreeNode(1)
bt.root.left = TreeNode(2)
bt.root.right = TreeNode(3)
bt.root.left.left = TreeNode(4)
bt.root.left.right = TreeNode(5)
bt.root.right.left = TreeNode(6)
bt.root.right.right = TreeNode(7)
bt.root.left.left.left = TreeNode(8)
bt.root.left.left.right = TreeNode(9)
bt.root.right.right.right = TreeNode(10)

# Test the traversals
print("Preorder Traversal:", bt.preorder_traversal())
print("Inorder Traversal:", bt.inorder_traversal())
print("Postorder Traversal:", bt.postorder_traversal())
  