class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        
        def edge_graph():
            graph = {1: defaultdict(list),\
                     -1: defaultdict(list)}
            
            for a, b in redEdges:
                graph[1][a].append(b)
                
        
            for u, v in blueEdges:
                graph[-1][u].append(v)
            
            return graph
        
        
        def bfs():
            answer[0] = 0
            q = deque([(0, 1), (0, -1)])
            seen = set([(0, 1), (0, -1)])
            path = 0
            
            while(q):
                path += 1
                for _ in range(len(q)):
                    node, color = q.popleft()
                    ac = -1 * color
                    for neigh in egraph[color][node]:
                        if((neigh, color) not in seen):
                            seen.add((neigh, color))
                            q.append((neigh, ac))
                            
                            if(answer[neigh] == -1):
                                answer[neigh] = path
        
        answer = [-1] * n
        egraph = edge_graph()
        bfs()
        return answer