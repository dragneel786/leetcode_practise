class Solution:
    def trap(self, height: List[int]) -> int:
        left = trapped = 0
        right = len(height) - 1
        
        left_max = height[left]
        right_max = height[right]
        
        while(left <= right):
            if(height[left] < height[right]):
                if(left_max > height[left]):
                    trapped += left_max - height[left]
                
                left_max = max(left_max, height[left])
                left += 1
            
            else:
                if(right_max > height[right]):
                    trapped += right_max - height[right]
                
                right_max = max(right_max, height[right])
                right -= 1
        
        return trapped
        
        
        
        