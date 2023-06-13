class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rmap = Counter([tuple(grid[i]) for i in range(len(grid))])
        n = len(grid)
        count = 0
        
        for c in range(n):
            t = []
            for r in range(n):
                t.append(grid[r][c])
                
            count += rmap.get(tuple(t), 0)
        
        return count
    # [[3,1,2,2],
    #  [1,4,4,5],
    #  [2,4,2,2],
    #  [2,4,2,2]]