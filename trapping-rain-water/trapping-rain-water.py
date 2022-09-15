class Solution:
    def trap(self, height: List[int]) -> int:
        left_max = [height[0]]
        for h in height[1:]:
            left_max.append(max(left_max[-1], h))
        
        total = 0
        maxr = height[-1]
        for j in range(len(height) - 2, -1, -1):
            val = min(maxr, left_max[j])
            if(height[j] < val):
                total += (val - height[j])
            
            maxr = max(height[j], maxr)
        
        return total
        
            