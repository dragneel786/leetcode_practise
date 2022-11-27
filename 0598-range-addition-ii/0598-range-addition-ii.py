class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        if(not ops):
            return m * n
        
        minx, miny = m, n
        for x, y in ops:
            minx = min(x, minx)
            miny = min(y, miny)
        
        return minx * miny
            
        
        
            
        
        