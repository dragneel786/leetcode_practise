class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        def dfs(x, y):
            visited.add((x, y))

            for dx, dy in direction:
                nx, ny = x + dx, y + dy
                if(0 <= nx < m and 0 <= ny < n\
                    and matrix[nx][ny] > matrix[x][y]):

                    if((nx, ny) not in visited):
                        memo[x][y] = max(dfs(nx, ny) + 1, memo[x][y])
                    else:
                        memo[x][y] = max(memo[nx][ny] + 1, memo[x][y])

            return memo[x][y]

        direction = [[0, 1], [1, 0],\
                        [-1, 0], [0, -1]]
        m, n = len(matrix), len(matrix[0])
        memo = [([1] * n) for _ in range(m)]
        max_len = -inf
        visited = set()

        for r in range(m):
            for c in range(n):
                if((r, c) not in visited):
                    dfs(r, c)

                max_len = max(memo[r][c], max_len)

        return max_len
                