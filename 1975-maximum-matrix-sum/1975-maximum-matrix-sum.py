class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        min_val = inf
        neg_count = tot = 0
        for m in matrix:
            for v in m:
                min_val = min(min_val, abs(v))
                if v < 0:
                    neg_count += 1
                
                tot += abs(v)
        
        if neg_count % 2 == 1:
            tot = tot - min_val - min_val
        
        return tot
        
        
                    