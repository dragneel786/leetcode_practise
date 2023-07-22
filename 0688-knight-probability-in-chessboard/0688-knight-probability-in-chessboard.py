class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        @lru_cache(None)
        def prob(remain_k, sr, sc):
            nonlocal n
            if(sr < 0 or sr >= n or sc < 0 or sc >= n):
                return 0
            
            if(not remain_k):
                return 1
            
            val = 0
            for dr, dc in [(2,1),(2,-1),(-2,1),(-2,-1),
                          (1,2),(1,-2),(-1,2),(-1,-2)]:
                nr, nc = sr + dr, sc + dc
                val += prob(remain_k - 1, nr, nc)
            
            return val / 8
        
        
        return prob(k, row, column)