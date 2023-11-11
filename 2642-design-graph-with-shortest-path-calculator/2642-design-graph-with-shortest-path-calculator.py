class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.graph = defaultdict(list)
        for e1, e2, cost in edges:
            self.graph[e1].append((e2, cost))
        self.size = n

    def addEdge(self, edge: List[int]) -> None:
        e1, e2, cost = edge
        self.graph[e1].append((e2, cost))

    def shortestPath(self, node1: int, node2: int) -> int:
        pq = [(0, node1)]
        dist = [inf] * self.size
        dist[node1] = 0
        
        while(pq):
            d, node = heappop(pq)
            if(node == node2): return d
            if(d > dist[node]): continue
                
            for new_node, cost in self.graph[node]:
                if(dist[new_node] > cost + d):
                    dist[new_node] = cost + d
                    heappush(pq, (cost + d, new_node))
        
        return -1


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)