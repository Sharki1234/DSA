class Graph:
    def __init__(self,node):
        self.n = node
        self.adj_list = [[]*self.n for i in range(self.n)]
    def add_edge(self,x,y):
        self.adj_list[x-1].append(y-1)
        self.adj_list[y-1].append(x-1)
    def bfs(self,source):
        result = []
        visited = [False]*self.n

        queue = []
        queue.append(source)
        while len(queue) >0:
            s = queue.pop()
            result.append(s)
            visited[source] = True
            for num in self.adj_list[s]:
                if visited[num] == False:
                    queue.append(num)
                    visited[num] = True
        return result
    def count_neighbours(self,node):
        return len(self.adj_list[node-1])


g = Graph(6)
g.add_edge(3,5)
g.add_edge(4,3)
g.add_edge(5,6)
print(g.bfs(3))
print(g.count_neighbours(3))
print(g.adj_list)

