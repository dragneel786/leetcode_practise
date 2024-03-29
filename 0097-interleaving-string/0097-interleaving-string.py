class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        l1, l2, l3 = len(s1), len(s2), len(s3)
        if(l1 + l2 != l3):
            return False
        l1, l2 = l1 + 1, l2 + 1
        dp = [([False] * l2) for _ in range(l1)]
        for i in range(l1):
            for j in range(l2):
                if(i == 0 and j == 0):
                    dp[i][j] = True
                    
                if(j > 0):
                    dp[i][j] |= (dp[i][j - 1] & (s2[j - 1] == s3[i + j - 1]))

                if(not dp[i][j] and i > 0):
                    dp[i][j] |= (dp[i - 1][j] & (s1[i - 1] == s3[i + j - 1]))
        
        return dp[l1 - 1][l2 - 1]
            
        
        