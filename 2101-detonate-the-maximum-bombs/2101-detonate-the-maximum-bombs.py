class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        
        def is_covered(x1, y1, x2, y2, r):
            return math.sqrt((x2 - x1)**2 + (y2 - y1)**2) <= r
        
        def create_graph():
            g = defaultdict(list)
            for i in range(len(bombs)):
                x1, y1, r1 = bombs[i]
                for j in range(i + 1, len(bombs)):
                    x2, y2, r2 = bombs[j]
                    if(is_covered(x1, y1, x2, y2, r1)):
                        g[i].append(j)
                    
                    if(is_covered(x2, y2, x1, y1, r2)):
                        g[j].append(i)
                        
            return g
        
        def dfs(start, visited):
            visited.add(start)
            
            count = 1
            for v in graph[start]:
                if(v not in visited):
                    count += dfs(v, visited)
            
            return count
            
        graph = create_graph()
        ans = 0
        for i in range(len(bombs)):
            ans = max(dfs(i, set()), ans)
        
        return ans
                        