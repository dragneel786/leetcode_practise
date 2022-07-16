class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:
        
        @lru_cache(None)
        def backtrack(dp):
            minHeight = math.inf
            start = 0
            for i, h in enumerate(dp):
                if(h < minHeight):
                    minHeight = h
                    start = i
            
            if(minHeight == n):
                return 0
            
            newDp = list(dp)
            ans = math.inf
            for end in range(start, m):
                width = end - start + 1
                if(dp[end] != minHeight or width + minHeight > n):
                    break 
                newDp[start: end + 1] = [width + minHeight] * width
                ans = min(ans, backtrack(tuple(newDp)) + 1)
            return ans
        
        dp = [0] * m
        return backtrack(tuple(dp))
            
                    