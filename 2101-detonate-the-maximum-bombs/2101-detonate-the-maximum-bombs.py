class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        
        intersects = lambda x, y: (x[2] ** 2) >= ((x[0] - y[0])**2)\
        + ((x[1] - y[1])**2)
        
        def construct_graph():
            g = defaultdict(list)
            
            for i in range(len(bombs)):
                for j in range(len(bombs)):
                    if(i == j): continue
                    if(intersects(bombs[i], bombs[j])):
                        g[i].append(j)
            
            return g
        
        
        def dfs(x, visited):
            res = 0
            visited.add(x)
            for v in graph[x]:
                if(v not in visited):
                    res += (1 + dfs(v, visited))
            return res
                    
        
        graph = construct_graph()
        max_value = -inf
        for i in range(len(bombs)):
            max_value = max(1 + dfs(i, set()), max_value)
            
        return max_value
        
                        