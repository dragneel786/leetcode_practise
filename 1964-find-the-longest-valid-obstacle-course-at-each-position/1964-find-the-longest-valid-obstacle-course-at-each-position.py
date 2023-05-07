class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        n = len(obstacles)
        ans = [inf] * n
        dp = ans.copy()
        for i in range(n):
            idx = bisect_right(dp, obstacles[i])
            ans[i] = idx + 1
            dp[idx] = obstacles[i]
            
        return ans
        
        