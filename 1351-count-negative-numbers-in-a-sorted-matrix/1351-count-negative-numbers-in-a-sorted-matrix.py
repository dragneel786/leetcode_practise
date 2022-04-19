class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        for g in grid:
            l = 0
            h = len(g) - 1
            i = -1
            while(l <= h):
                m = l + (h - l) // 2
                if(g[m] < 0):
                    i = m
                    h = m - 1
                else:
                    l = m + 1
                    
            if(i != -1):
                count += (len(g) - i)
        
        return count
            