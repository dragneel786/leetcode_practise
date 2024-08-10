class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        
        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                parent[py] = find(px)
                return False
            
            return True
        
        
        def find(x): 
            if x != parent[x]:
                parent[x] = find(parent[x])
                
            return parent[x]
            
    
        n = len(grid) + 1
        parent = {i: i for i in range(n * n)}
        for i in range(n):
            for j in range(n):
                index = (n * i + j)
                if i == 0 or i == n - 1 or j == 0 or j == n - 1:
                    parent[index] = 0
        
        
        ans = 1
        for r, g in enumerate(grid):
            for c, s in enumerate(g):
                if s == '/':
                    a = ((r + 1) * n + c)
                    b = (r * n + (c + 1))
                    ans += union(a, b)
                elif s == '\\':
                    a = (r * n + c)
                    b = ((r + 1) * n + (c + 1))
                    ans += union(a, b)
        return ans