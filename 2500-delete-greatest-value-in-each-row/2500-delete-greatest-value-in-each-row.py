class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        for g in grid:
            heapify(g)
        
        ans = 0
        for c in range(len(grid[0])):
            max_v = 0
            for r in range(len(grid)):
                max_v = max(max_v, heappop(grid[r]))
            
            ans += max_v
        
        return ans