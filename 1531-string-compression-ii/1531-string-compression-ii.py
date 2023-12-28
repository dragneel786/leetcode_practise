class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        
        def count_del(cnt):
            if(cnt >= 100):
                return 3
            
            if(cnt >= 10):
                return 2
            
            if(cnt >= 2):
                return 1
            
            return 0
        
        n = len(s)
        dp = [([9999] * (k + 1)) for _ in range(n + 1)]
        dp[0][0] = 0
        for i in range(1, n + 1):
            for j in range(k + 1):
                count = del_ = 0
                for l in range(i, 0, -1):
                    if(s[i - 1] == s[l - 1]):
                        count += 1
                    else:
                        del_ += 1
                    
                    if(j - del_ >= 0):
                        dp[i][j] = min(dp[i][j], dp[l - 1][j - del_] + 1\
                                       + count_del(count))
            
                if(j > 0):
                    dp[i][j] = min(dp[i][j], dp[i - 1][j - 1])
        
        return dp[n][k]
                    
                    
                        
                        