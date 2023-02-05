class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)
        dp = [inf] * (n + 1)
        dp[0] = 0
        for i in range(1, n + 1):
            for c, d in zip(costs, [0, 6, 29]):
                j = i - 1
                while(j > 0 and days[j - 1] >= days[i - 1] - d):
                    j -= 1
                
                dp[i] = min(dp[i], dp[j] + c)
            
        return dp[n]