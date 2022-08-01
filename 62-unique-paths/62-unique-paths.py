class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        @lru_cache(None)
        def paths(i, j):
            if(i == m - 1 and j == n - 1): return 1
            if(i >= m or j >= n): return 0

            return paths(i + 1, j) + paths(i, j + 1)

        
        return paths(0, 0)