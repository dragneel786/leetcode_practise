class Solution:
    def coloredCells(self, n: int) -> int:
        if(n == 1):
            return 1
        
        start = 1
        for i in range(n):
            start += (4 * i)
        
        return start
            
        