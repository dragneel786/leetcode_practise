class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        def paths(i, j, memo={}):
            key = (i, j)
            if(key in memo): return memo[key]
            if(i == m - 1 and j == n - 1): return 1
            if(i >= m or j >= n): return 0

            memo[key] = paths(i + 1, j) + paths(i, j + 1)
            return memo[key]

        
        return paths(0, 0)