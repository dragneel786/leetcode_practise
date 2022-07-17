class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        
        def createInversePairs(n, k):
            dp = [([0] * (k + 1)) for _ in range(n + 1)]
            for i in range(1, n + 1):
                val = 0
                for j in range(min(k, i * (i - 1) // 2) + 1):
                    if(j == 0):
                        dp[i][j] = 1
                    else:
                        val = (dp[i - 1][j] + M - (dp[i - 1][j - i] if((j - i) >= 0) else 0)) % M
                        dp[i][j] = (dp[i][j - 1] + val) % M
            return dp[n][k] % M

        M = (10 ** 9) + 7
        return createInversePairs(n, k)

    
        
                    
                
        