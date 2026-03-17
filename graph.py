class Graph:
    def __init__(self,node):
        self.node = node
        self.adj_list = [[]for i in range(node)]

graph = Graph(7)
print(graph.adj_list)