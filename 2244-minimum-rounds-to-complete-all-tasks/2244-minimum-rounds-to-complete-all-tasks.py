class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        freq_val = Counter(Counter(tasks).values())
        if(1 in freq_val):
            return -1
        
        n = max(3, max(freq_val.keys())) + 1
        ans = 0
        dp = [inf] * n
        dp[0] = 0
        for i in range(2, n):
            dp[i] = min(dp[i - 2], dp[i - 3]) + 1
            if(i in freq_val):
                ans += dp[i] * freq_val[i]

        return ans
        
        
        
        
                
        
        
        