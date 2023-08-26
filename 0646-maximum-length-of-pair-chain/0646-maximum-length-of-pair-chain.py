class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        
        pairs.sort()
        n = len(pairs)
        dp = [1] * n
        res = 1
        for i in range(1, n):
            max_v = 0
            for j in range(i):
                if(pairs[j][1] < pairs[i][0]):
                    max_v = max(max_v, dp[j])
            
            dp[i] = max_v + 1
            res = max(dp[i], res)
        
        return res
        
                