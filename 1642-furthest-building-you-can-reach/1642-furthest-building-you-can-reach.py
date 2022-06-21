class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        maxJump = []
        b = 0
        heights = heights + [0]
        for i in range(1, len(heights)):
            diff = heights[i] - heights[i - 1]
            if(diff > 0):
                heappush(maxJump, diff)
                if(len(maxJump) > ladders):
                    b += heappop(maxJump)
                    if(b > bricks):
                        break
                
        return i - 1