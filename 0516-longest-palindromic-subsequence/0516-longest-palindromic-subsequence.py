class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n + 1)
        large = 0
        rev_s = s[::-1]
        for i in range(1, n + 1):
            temp = [0] * (n + 1)
            for j in range(1, n + 1):
                if(s[i - 1] == rev_s[j - 1]):
                    temp[j] = dp[j - 1] + 1
                else:
                    temp[j] = max(dp[j], temp[j - 1])
            
            large = max(temp)
            dp = temp
        
        return large
            