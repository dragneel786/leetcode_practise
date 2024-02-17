class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        
        max_jumps = []
        heights.append(0)
        for i in range(1, len(heights)):
            diff = heights[i] - heights[i - 1]
            if(diff <= 0):
                continue
                
            heappush(max_jumps, diff)
            if(len(max_jumps) > ladders):
                bricks -= heappop(max_jumps)
            
            if(bricks < 0):
                break
        
        
        return i - 1
        