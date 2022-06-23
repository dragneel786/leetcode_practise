class Solution:
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        dire = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        parent = [i for i in range(R * C)]
        scores = [(x, y) for x in range(R) for y in range(C)]
        seen = [[0 for _ in range(C)] for _ in range(R)]
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            rx, ry = find(x), find(y)
            if(rx != ry):
                parent[ry] = rx
        
        scores.sort(key=lambda s: grid[s[0]][s[1]], reverse=True)
        for x, y in scores:
            seen[x][y] = 1
            for dx, dy in dire:
                nx, ny = x + dx, y + dy
                if(0 <= nx < R and 0 <= ny < C and seen[nx][ny]):
                    union(x * C + y, nx * C + ny)
            if(find(0) == find(R * C - 1)):
                return grid[x][y]
        
        return -1
        