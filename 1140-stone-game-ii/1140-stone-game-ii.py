class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        
        @lru_cache(None)
        def max_stone(alice, i, M):
            if(i >= len(piles)):
                return 0
            
            res = 0 if(alice) else inf
            tot = 0
            for j in range(1, 2 * M  + 1):
                if(i + j > len(piles)):
                    break
                
                tot += piles[i + j - 1]
                val = max_stone(not alice, i + j, max(M, j))
                res = max(res, tot + val) if(alice) else min(res, val)
            
            return res
            
        
        return max_stone(True, 0, 1)