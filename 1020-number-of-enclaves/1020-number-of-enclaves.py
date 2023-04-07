class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        
        def dfs(r, c):
            nonlocal rows, cols, is_valid
            if(r < 0 or r >= rows or\
               c < 0 or c >= cols):
                is_valid = False
                return 0
            
            if(not grid[r][c]):
                return 0
            
            grid[r][c] = 0
            return 1 + dfs(r + 1, c) + dfs(r, c + 1) \
        + dfs(r - 1, c) + dfs(r, c - 1)

        
        
        rows, cols = len(grid), len(grid[0])
        ans = 0 
        for r in range(rows):
            for c in range(cols):
                if(grid[r][c]):
                    is_valid = True
                    val = dfs(r, c)
                    if(is_valid):
                        ans += val
                    
        return ans
            
            
        
        
        
#         def union(x, y):
#             px, py = find(x), find(y)
#             parent[max(px, py)] = min(px, py)
        
        
#         def find(x):
#             if(parent[x] != x):
#                 parent[x] = find(parent[x])
#             return parent[x]
        
        
#         parent = {-1:-1}
#         rows, cols = len(grid), len(grid[0])
#         for r in range(rows):
#             for c in range(cols):
#                 if(grid[r][c]):
#                     cell = (r * rows) + c
#                     parent[cell] = cell
#                     if(r == 0 or r == rows - 1 or \
#                        c == 0 or c == cols - 1):
#                         parent[cell] = -1

#                     nr, nc = r - 1, c - 1
#                     if(nr >= 0 and grid[nr][c]):
#                         new_cell = (nr * rows) + c
#                         union(new_cell, cell)

#                     if(nc >= 0 and grid[r][nc]):
#                         new_cell = (r * rows) + nc
#                         union(new_cell, cell)
        
#         counts = 0
#         for k in parent.keys():
#             if find(k) != -1:
#                 print(k, parent[k])
#             counts += (find(k) != -1)
        
#         return counts
                
                
        