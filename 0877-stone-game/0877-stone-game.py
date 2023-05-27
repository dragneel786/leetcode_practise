class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        
        @lru_cache(None)
        def check_win(alice, i, j):
            if(i > j):
                return 0
            
            val1 = piles[i] + check_win(not alice, i + 1, j)
            val2 = piles[j] + check_win(not alice, i, j - 1)
            if(alice):
                return max(val1, val2)
            else:
                return min(val1, val2)
            
        
        val = check_win(True, 0, len(piles) - 1)
        sums = sum(piles)
        return val > sums-val