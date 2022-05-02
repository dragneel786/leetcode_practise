class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        low = 1
        high = position[-1]
        
        def isValid(gap):
            placed = 1
            prev = position[0]
            for p in range(1, len(position)):
                if(position[p] - prev >= gap):
                    prev = position[p]
                    placed += 1
                    if(placed == m):
                        return True
            return False
                    
        ans = 0
        while(low <= high):
            mid = (high - low) // 2 + low
            if(isValid(mid)):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        
        return ans
                