class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        
        def make_graph():
            g = {i:[i + 1] for i in range(n - 1)}
            g[n - 1] = []
            return g
        
        def bfs():
            q = deque([0])
            visited = set([0])
            steps = 0
            while(q):
                for _ in range(len(q)):
                    node = q.popleft()
                    if node == n - 1:
                        return steps
                    
                    for v in graph[node]:
                        if v not in visited:
                            q.append(v)
                            visited.add(v)
                
                steps += 1
                    
        
        graph = make_graph()
        res = []
        for a, b in queries:
            graph[a].append(b)
            res.append(bfs())
        
        return res