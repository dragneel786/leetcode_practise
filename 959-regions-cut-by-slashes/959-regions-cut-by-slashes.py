class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        parents = {}
        
        def find(x):
            parents.setdefault(x, x)
            if(x != parents[x]):
                x = find(parents[x])
            return x
        
        def union(x, y):
            parents[find(y)] = x
        
        dots = n + 1
        for i in range(dots):
            for j in range(dots):
                if(not i or not j or\
                   i == dots - 1 or j == dots - 1):
                    union(0, (i * dots) + j)
        
        def connect(x, y):
            nonlocal counts
            if(find(x) == find(y)):
                counts += 1
            else:
                union(x, y)
            
        
        counts = 1
        for i in range(n):
            for j in range(n):
                if(grid[i][j] == ' '): continue
                x, y = 0, 0
                if(grid[i][j] == '/'):
                    x, y = ((i + 1) * dots + j), (i * dots + (j + 1))
                elif(grid[i][j] == '\\'):
                    x, y = (i * dots + j), ((i + 1) * dots + (j + 1))
                
                connect(x, y)
                
                
        return counts
                
                
                
                
                
                