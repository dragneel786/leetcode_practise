class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dp = [([math.inf] * n) for _ in range(n)]
        dp[0][0] = grid[0][0]
        q = deque([(0, 0)])
        while(q):
            for _ in range(len(q)):
                x, y = q.popleft()
                for dx, dy in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                    nx, ny = x + dx, y + dy
                    if(0 <= nx < n and 0 <= ny < n):
                        val = max(dp[x][y], grid[nx][ny])
                        if(dp[nx][ny] > val):
                            dp[nx][ny] = val
                            q.append((nx, ny))

        return dp[n - 1][n - 1]
            
                