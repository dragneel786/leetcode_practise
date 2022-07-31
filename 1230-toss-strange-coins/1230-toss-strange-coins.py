class Solution:
    def probabilityOfHeads(self, prob: List[float], target: int) -> float:
        dp = [1] + [0] * target
        for i,p in enumerate(prob):
            for t in range(min(target, i + 1), -1 , -1):
                dp[t] = ((dp[t - 1] if(t) else 0) * p) + (dp[t] * (1 - p))
        
        return dp[target]
            
            