class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        
        def prefix_sum(piles):
            for pile in piles:
                for i in range(1, len(pile)):
                    pile[i] += pile[i - 1]
        
        
        @lru_cache(None)
        def get_max_value(i, remain):
            nonlocal n
            if(not remain):
                return 0
            
            if(i >= n):
                return -inf
                
            
            max_val = 0
            m = len(piles[i])
            for j in range(min(remain, m) + 1):
                add_coins = 0 
                if(j > 0):
                    add_coins = piles[i][j - 1]
                
                max_val = max(max_val, add_coins\
                              + get_max_value(i + 1, remain - j))
            
            return max_val
                
        
        n = len(piles)
        prefix_sum(piles)
        return get_max_value(0, k)
            