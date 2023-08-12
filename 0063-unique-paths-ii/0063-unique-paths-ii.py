class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        @lru_cache(None)
        def possible_paths(i, j):
            # print(i, j, obstacleGrid[i][j], m, n)
            if(i >= m or j >= n or obstacleGrid[i][j]):
                return 0
            
            if(i == m - 1 and j == n - 1):
                return 1
            
            return possible_paths(i + 1, j) +\
        possible_paths(i, j + 1)
        
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        return possible_paths(0, 0)