class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        def dfs(x, y):
            if(memo[x][y] != 0):
                return memo[x][y]
            
            for dx, dy in direction:
                nx, ny = x + dx, y + dy
                if(0 <= nx < m and 0 <= ny < n\
                    and matrix[nx][ny] > matrix[x][y]):
                    memo[x][y] = max(dfs(nx, ny), memo[x][y])
            
            memo[x][y] += 1
            return memo[x][y]

        direction = [[0, 1], [1, 0],\
                        [-1, 0], [0, -1]]
        m, n = len(matrix), len(matrix[0])
        memo = [([0] * n) for _ in range(m)]
        max_len = -inf
        for r in range(m):
            for c in range(n):
                if(not memo[r][c]):
                    dfs(r, c)
                max_len = max(memo[r][c], max_len)

        return max_len
                