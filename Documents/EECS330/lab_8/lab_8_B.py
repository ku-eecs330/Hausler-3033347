class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adjacency_list = [[] for _ in range(vertices)]

    def add_edge(self, u, v):
        self.adjacency_list[u].append(v)
        self.adjacency_list[v].append(u)

    def dfs(self, source):
        visited = [False] * self.vertices
        result = []

        def dfs_util(node):
            visited[node] = True
            result.append(node)
            for neighbor in self.adjacency_list[node]:
                if not visited[neighbor]:
                    dfs_util(neighbor)

        dfs_util(source)
        return result

    def bfs(self, source):
        visited = [False] * self.vertices
        result = []
        queue = []

        visited[source] = True
        queue.append(source)

        while queue:
            node = queue.pop(0)
            result.append(node)
            for neighbor in self.adjacency_list[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)

        return result

# Create a graph with 20 vertices
graph = Graph(20)

# Add edges (change as needed)
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 3)
graph.add_edge(1, 4)
graph.add_edge(2, 5)
graph.add_edge(2, 6)
graph.add_edge(3, 7)
graph.add_edge(3, 8)
graph.add_edge(4, 9)
graph.add_edge(4, 10)
graph.add_edge(5, 11)
graph.add_edge(5, 12)
graph.add_edge(6, 13)
graph.add_edge(6, 14)
graph.add_edge(7, 15)
graph.add_edge(7, 16)
graph.add_edge(8, 17)
graph.add_edge(8, 18)
graph.add_edge(9, 19)

# Test DFS and BFS from a source vertex
print("DFS from vertex 0:", graph.dfs(0))  
print("BFS from vertex 0:", graph.bfs(0))

# Create a graph with 4 vertices
graph = Graph(4)
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 2)
graph.add_edge(2, 0)
graph.add_edge(2, 3)
graph.add_edge(3, 3)

# Test DFS and BFS from a source vertex
print("DFS from vertex 2:", graph.dfs(2))
print("BFS from vertex 2:", graph.bfs(2))
