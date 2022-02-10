class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if(n < 2):
            return n
        
        dp = [0, 1]
        i = 1
        large = 1
        j = 2
        while(j <= n):
            dp.append(dp[i])
            j += 1
            if(j > n):
                break
            dp.append(dp[i] + dp[i + 1])
            large = max(large, max(dp[-1], dp[-2]))
            i += 1
            j += 1
        
        return large