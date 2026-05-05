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
            s = queue.pop(0)
            result.append(s+1)
            visited[source] = True
            for num in self.adj_list[s]:
                if visited[num] == False:
                    queue.append(num)
                    visited[num] = True
        return result
    def utiliser(self,source,visited,result):
        result.append(source+1)
        visited[source] = True
        for node in self.adj_list[source]:
            if not visited[node]:
                self.utiliser(node,visited,result)

    # def dfs2(self,source,visited):
    #     if source not in visited:
    #         print(source)

    #         visited.append(source)
    #     for node in self.adj_list[source]:
    #         if node not in visited:
    #             self.dfs2(node,visited)
        

    def dfs(self,source):
        result = []
        self.visited = [False]*self.n
        self.utiliser(source-1,self.visited,result)
        return result
    def count(self):
        included = []
        for n in self.adj_list:
            for i in n:
                if i not in included:
                    included.append(i)
        for j in range(len(self.adj_list)):
            if j not in included:
                print(j+1)
        
g = Graph(6)
g.add_edge(3,5)
g.add_edge(4,3)
g.add_edge(5,6)
g.add_edge(2,6)
g.add_edge(1,4)
#print(g.bfs(3))
print(g.dfs(3))
g.count()

#print(g.dfs(3))




