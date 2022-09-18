class Solution:
    def trap(self, height: List[int]) -> int:
        
        n = len(height)
        left_max = [height[0]] * n
        
        for i, h in enumerate(height[1:], 1):
            left_max[i] = max(left_max[i - 1], h)
        
        
        max_r = height[-1]
        trapped = 0
        
        for i in range(n - 2, 0, -1):
            h =  height[i]
            max_r = max(max_r, h)
            
            if(h < min(left_max[i], max_r)):
                trapped += (min(left_max[i], max_r) - h)
            
        return trapped
        