class Node:
    def __init__(self, value):
        self.value = value  
        self.left = None  
        self.right = None   

class BinaryTree:
    def __init__(self):
        self.root = None  

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)  
        else:
            self._insert(self.root, value)  

    def _insert(self, node, value):
        
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert(node.left, value)  # Recursively go left
        else:  # If value is greater or equal, insert to the right
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert(node.right, value)  # Recursively go right

    # Inorder traversal (Left, Root, Right)
    def inorder_traversal(self):
        result = []
        self._inorder_traversal(self.root, result)
        return result

    def _inorder_traversal(self, node, result):
        if node is not None:
            self._inorder_traversal(node.left, result)  # Traverse left
            result.append(node.value)  # Add root value
            self._inorder_traversal(node.right, result)  # Traverse right

# Example usage
tree = BinaryTree()
tree.insert(10)
tree.insert(5)
tree.insert(15)
tree.insert(3)
tree.insert(7)
tree.insert(13)
tree.insert(18)

# Inorder traversal (this will give sorted values)
print("Inorder Traversal:", tree.inorder_traversal())
