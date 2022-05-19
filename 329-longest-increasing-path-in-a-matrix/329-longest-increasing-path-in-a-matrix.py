class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        dp = [([1] * cols) for _ in range(rows)]
        visited = set()
        dir = [[1,0], [0,1], [-1,0], [0,-1]]

        def dfs(r, c, seen = set()):
            seen.add((r,c))
            maxV = 0
            for di, dj in dir:
                x = r + di
                y = c + dj
                if((x, y) in visited and matrix[r][c] < matrix[x][y]):
                    maxV = max(maxV, dp[x][y])
                elif(0 <= x < rows and 0 <= y < cols and\
                     (x, y) not in seen and\
                          matrix[r][c] < matrix[x][y]):
                    dfs(x, y, seen)
                    maxV = max(maxV, dp[x][y])

            dp[r][c] += maxV
            visited.add((r,c))

        longest = 0
        for r in range(rows):
            for c in range(cols):
                if((r, c) not in visited):
                    dfs(r, c)
                longest = max(longest, dp[r][c])

        return longest