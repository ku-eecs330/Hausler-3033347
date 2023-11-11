class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def add_edge(self, u, v, w):
        self.graph[u][v] = w
        self.graph[v][u] = w

    def dijkstra(self, src):
        dist = [float('inf')] * self.V
        dist[src] = 0
        visited = [False] * self.V
        for _ in range(self.V):
            u = self.min_distance(dist, visited)
            visited[u] = True
            for v in range(self.V):
                if not visited[v] and self.graph[u][v] > 0 and dist[v] > dist[u] + self.graph[u][v]:
                    dist[v] = dist[u] + self.graph[u][v]
        self.print_dijkstra(dist)

    def min_distance(self, dist, visited):
        min_dist = float('inf')
        min_index = -1
        for v in range(self.V):
            if dist[v] < min_dist and not visited[v]:
                min_dist = dist[v]
                min_index = v
        return min_index

    def print_dijkstra(self, dist):
        print("Vertex \t Distance from Source")
        for node in range(self.V):
            print(f"{node} \t->\t {dist[node]}")

    def prim(self):
        key = [float('inf')] * self.V
        result = [None] * self.V
        key[0] = 0
        mst_set = [False] * self.V
        for _ in range(self.V):
            u = self.min_key(key, mst_set)
            mst_set[u] = True
            for v in range(self.V):
                if 0 < self.graph[u][v] < key[v] and not mst_set[v]:
                    key[v] = self.graph[u][v]
                    result[v] = u
        self.print_prim(result)

    def min_key(self, key, mst_set):
        min_val = float('inf')
        min_index = -1
        for v in range(self.V):
            if key[v] < min_val and not mst_set[v]:
                min_val = key[v]
                min_index = v
        return min_index
    
    def print_prim(self, result):
        print("Edge \t Weight")
        for i in range(1, self.V):
            print(f"{result[i]} - {i} \t {self.graph[i][result[i]]}")

    def kruskal_mst(self):
        result = []
        edges = []
        for i in range(self.V):
            for j in range(i + 1, self.V):
                if self.graph[i][j] != 0:
                    edges.append((i, j, self.graph[i][j]))
        edges.sort(key=lambda edge: edge[2])
        parent = [i for i in range(self.V)]
        for edge in edges:
            x, y, w = edge
            x_set = self.find(parent, x)
            y_set = self.find(parent, y)
            if x_set != y_set:
                result.append(edge)
                self.union(parent, x_set, y_set)
        self.print_kruskal(result)

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, x, y):
        parent[x] = y

    def print_kruskal(self, result):
        print("Edge \t Weight")
        for edge in result:
            print(f"{edge[0]} -> {edge[1]} \t {edge[2]}")


# Create a graph with 21 vertices.
graph = Graph(21)

# Add edges and their weights.
graph.add_edge(0, 1, 4)
graph.add_edge(0, 2, 1)
graph.add_edge(1, 3, 3)
graph.add_edge(2, 4, 2)
graph.add_edge(3, 5, 2)
graph.add_edge(4, 6, 2)
graph.add_edge(5, 7, 2)
graph.add_edge(7, 8, 2)
graph.add_edge(6, 8, 2)

graph.add_edge(8, 9, 5)
graph.add_edge(8, 10, 4)
graph.add_edge(9, 11, 3)
graph.add_edge(10, 11, 1)

graph.add_edge(11, 12, 1)
graph.add_edge(12, 13, 1)
graph.add_edge(13, 14, 1)

graph.add_edge(14, 15, 1)
graph.add_edge(14, 16, 10)
graph.add_edge(15, 17, 1)
graph.add_edge(16, 20, 1)
graph.add_edge(17, 18, 1)
graph.add_edge(18, 19, 1)
graph.add_edge(19, 20, 1)

# Run Dijkstra's algorithm from source vertex 0.
graph.dijkstra(0)

# Find and print the Prim's Minimum Spanning Tree (MST).
graph.prim()

# Find and print the Kruskal's Minimum Spanning Tree (MST).
graph.kruskal_mst()