class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def bfs(x, y):
            q = deque([(x, y)])
            ones = 1
            while(q):
                for _ in range(len(q)):
                    x, y = q.popleft()
                    for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                        nx, ny = x + dx, y + dy
                        if(0 <= nx < m and 0 <= ny < n and grid[nx][ny]):
                            grid[nx][ny] = 0
                            ones += 1
                            q.append((nx, ny))
            return ones
            
        res = 0
        m, n = len(grid), len(grid[0])
        for r in range(m):
            for c in range(n):
                if(grid[r][c]):
                    grid[r][c] = 0
                    res = max(res, bfs(r, c))
        return res