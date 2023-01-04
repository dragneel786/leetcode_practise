class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        freq_val = list(Counter(tasks).values())
        maxv, minv = max(freq_val), min(freq_val)
        
        if(minv == 1):
            return -1
        
        def calculate_min(n):
            dp = [inf] * n
            dp[2] = dp[3] = 1
        
            for i in range(4, n):
                dp[i] = min(dp[i - 2], dp[i - 3]) + 1
            
            return dp
        
        
        ans = 0
        min_rounds = calculate_min(max(maxv + 1, 4))
        for f in freq_val:
            ans += min_rounds[f]
        
        return ans
        
                
        
        
        