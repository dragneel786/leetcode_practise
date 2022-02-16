class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [1] * n
        s = 1
        for i in range(1, n):
            if(prices[i] + 1 == prices[i - 1]):
                dp[i] += dp[i - 1]
            s += dp[i]
            
        return s