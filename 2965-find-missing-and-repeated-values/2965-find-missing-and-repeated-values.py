class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        values = set([i for i in range(1, n * n + 1)])
        ret = [0, 0]
        for g in grid:
            for a in g:
                if(a not in values):
                    ret[0] = a
                
                values.discard(a)
        
        ret[1] = list(values)[0]
        return ret