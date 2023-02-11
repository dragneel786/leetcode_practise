class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        
        def edge_graph():
            graph = {'R': defaultdict(list),\
                     'B': defaultdict(list)}
            
            for a, b in redEdges:
                graph['R'][a].append(b)
                
        
            for u, v in blueEdges:
                graph['B'][u].append(v)
            
            return graph
        
        
        def bfs():
            answer[0] = 0
            q = deque([(0, 'R'), (0, 'B')])
            seen = set([(0, 'R'), (0, 'B')])
            path = 0
            
            while(q):
                path += 1
                for _ in range(len(q)):
                    node, color = q.popleft()
                    ac = alternate_color(color)
                    for neigh in egraph[color][node]:
                        if((neigh, color) not in seen):
                            seen.add((neigh, color))
                            q.append((neigh, ac))
                            
                            if(answer[neigh] == -1):
                                answer[neigh] = path
                
                            
            # for i in range(len(answer)):
            #     if(answer[i] == inf):
            #         answer[i] = -1
        
        alternate_color = lambda x: 'B' if(x == 'R') else 'R'
        answer = [-1] * n
        egraph = edge_graph()
        bfs()
        return answer