class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        def create_graph():
            g = defaultdict(list)
            for (a, b), v in zip(equations, values):
                g[a].append([b, v])
                g[b].append([a, 1 / v])
            return g
        
        
        def traverse(start):
            nonlocal end
            if(start == end):
                return 1
            
            visited.add(start)
            for v, d in graph[start]:
                if(v not in visited):
                    temp_ret = traverse(v)
                    if(temp_ret > 0):
                        return d * temp_ret
              
            visited.discard(start)
            return -1
            
        
        graph = create_graph()
        ans = []
        visited = set()
        for start, end in queries:
            if(start in graph):
                visited.clear()
                ans.append(traverse(start))
            else:
                ans.append(-1)
            
        return ans