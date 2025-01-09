
class Graphs:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

        if v not in self.graph:
            self.graph[v] = []
        self.graph[v].append(u)

    def display_graph(self):
        for node, edges in self.graph.items():
            print(f"{node} {edges}")

    def bfs(self, start):
        visited = set()
        queue = [start]

        while queue:
            node = queue.pop(0)  
            if node not in visited:
                print(node, end=" ")  
                visited.add(node)

                for neighbor in self.graph[node]:
                    if neighbor not in visited:
                        queue.append(neighbor)

    def dfs(self, start, visited=None):
        if visited is None:
            visited = set()
        print(start, end=" ")  
        visited.add(start)
        for neighbor in self.graph[start]:
            if neighbor not in visited:
                self.dfs(neighbor, visited)


g = Graphs()
g.add_edge(0,1)
g.add_edge(0,2)
g.add_edge(1,2)
g.add_edge(2,0)
g.add_edge(2,3)
g.add_edge(3,3)

print("Graph:")
g.display_graph()

print("\nBFS starting from node 0:")
g.bfs(2)

print("\nDFS starting from node 0:")
g.dfs(2)
