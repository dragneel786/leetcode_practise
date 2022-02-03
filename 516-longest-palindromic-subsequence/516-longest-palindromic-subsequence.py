class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n + 1)
        rev_s = s[::-1]
        large = 0
        for i in range(1, n + 1):
            temp = [0] * (n + 1)
            for j in range(1, n + 1):
                if(s[i - 1] == rev_s[j - 1]):
                    temp[j] = dp[j - 1] + 1
                else:
                    temp[j] = max(temp[j - 1], dp[j])
                
                large = max(temp[j], large)
            dp = temp
        
        return large
        
            