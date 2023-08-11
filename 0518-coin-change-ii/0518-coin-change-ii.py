class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        @lru_cache(None)
        def check(i, val):
            if(val == 0):
                return 1
            
            if(val < 0 or i >= len(coins)):
                return 0
            
            ret = check(i + 1, val)
            if(val >= coins[i]):
                ret += check(i, val - coins[i])
            
            return ret
            
        return check(0, amount)
            
                
        