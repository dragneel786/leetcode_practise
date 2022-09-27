class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        @lru_cache(None)
        def calculate(amount):
            if(not amount):
                return 0
            
            if(amount < -1):
                return inf
            
            ret = inf
            for c in coins:
                if(c > amount): break
                ret = min(ret, 1 + calculate(amount - c))
        
            return ret
        
        coins.sort()
        val = calculate(amount)
        return -1 if(val == inf) else val