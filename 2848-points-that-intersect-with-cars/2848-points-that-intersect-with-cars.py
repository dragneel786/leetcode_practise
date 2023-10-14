class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        dp = [0] * 102
        size = 0
        for s, e in nums:
            dp[s] += 1
            dp[e + 1] -= 1
            size = max(size, e)
        
        for i in range(1, 102):
            dp[i] += dp[i - 1]
        
        
        return sum([dp[d] > 0 for d in range(size + 1)])