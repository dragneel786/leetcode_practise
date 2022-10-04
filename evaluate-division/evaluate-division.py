class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        def equation_graph():
            graph = defaultdict(list)
            for (a, b), value in zip(equations, values):
                graph[a].append((b, value))
                graph[b].append((a, 1 / value))
            
            return graph
        
        
        def compute(src, dest):
            if(src not in eq_graph):
                return -1.0
                
            q = deque([(src, 1.0)])
            visited = set()
            
            while(q):
                for _ in range(len(q)):
                    var, val = q.popleft()
                    if(var == dest):
                        return val
                    
                    for nvar, nval in eq_graph[var]:
                        if(nvar not in visited):
                            visited.add(nvar)
                            q.append((nvar, val * nval))
            
            return -1.0
            
        
        eq_graph = equation_graph()
        res = []
        
        for s, d in queries:
            res.append(compute(s, d))
        
        return res