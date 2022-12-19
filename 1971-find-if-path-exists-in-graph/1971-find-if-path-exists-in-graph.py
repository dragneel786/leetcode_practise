class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        def create_graph():
            g = defaultdict(list)
            for a, b in edges:
                g[a].append(b)
                g[b].append(a)
            
            return g
        
        
        def bfs(graph):
            q = deque([source])
            visited = [True] * n
            while(q):
                node = q.popleft()
                if(node == destination):
                    return True
                
                for v in graph[node]:
                    if(visited[v]):
                        q.append(v)
                        visited[v] = False
            
            return False
                    
        graph = create_graph()
        return bfs(graph)
                
            