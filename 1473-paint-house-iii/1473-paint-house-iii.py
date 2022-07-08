class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        
        def paintIt(i, t, p):
            key = (i, t, p)
            if(i == m or t < 0 or m - i < t):
                return 0 if(t == 0 and i == len(houses)) else math.inf
            
            if(key not in dp):
                if(not houses[i]):
                    dp[key] = min(paintIt(i + 1, t - (p != j + 1), j + 1)\
                                  + cost[i][j] for j in range(n))
                else:
                    dp[key] = paintIt(i + 1, t - (p != houses[i]), houses[i])
                    
            return dp[key]
        
        dp = {}
        res = paintIt(0, target, -1)
        return res if(res != math.inf) else -1