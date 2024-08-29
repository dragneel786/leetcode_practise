class Solution:
    def maxArea(self, height: List[int]) -> int:
        start = res = 0
        end = len(height) - 1
        
        while(start < end):
            res = max(res, (end - start) * min(height[start], height[end]))
            if height[start] < height[end]:
                start += 1
            else:
                end -= 1
            
        return res