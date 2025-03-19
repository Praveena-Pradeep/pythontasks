from collections import deque

# Define the Node for the binary tree
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Binary Tree class
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
                self._insert(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert(node.right, value)

    # Breadth-First Search (BFS) for Binary Tree
    def bfs(self):
        if not self.root:
            return []

        result = []
        queue = deque([self.root])

        while queue:
            current_node = queue.popleft()
            result.append(current_node.value)
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
        return result

# Graph class for traversal
class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    # Breadth-First Search (BFS) for Graph
    def bfs(self, start):
        visited = set()
        queue = deque([start])
        visited.add(start)

        result = []
        while queue:
            node = queue.popleft()
            result.append(node)

            for neighbor in self.graph.get(node, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return result

    # Depth-First Search (DFS) for Graph
    def dfs(self, start):
        visited = set()
        result = []
        self._dfs(start, visited, result)
        return result

    def _dfs(self, node, visited, result):
        visited.add(node)
        result.append(node)
        for neighbor in self.graph.get(node, []):
            if neighbor not in visited:
                self._dfs(neighbor, visited, result)

# Example usage for Binary Tree BFS
tree = BinaryTree()
tree.insert(10)
tree.insert(5)
tree.insert(15)
tree.insert(3)
tree.insert(7)
tree.insert(13)
tree.insert(18)

print("Binary Tree BFS:", tree.bfs())

# Example usage for Graph BFS and DFS
graph = Graph()
graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(2, 4)
graph.add_edge(2, 5)
graph.add_edge(3, 6)

print("Graph BFS starting from node 1:", graph.bfs(1))  
print("Graph DFS starting from node 1:", graph.dfs(1))  
