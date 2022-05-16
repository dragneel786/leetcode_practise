class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        i = 0
        j = n - 1
        maxA = 0
        while(i < j):
            computed = min(height[i], height[j]) * (j - i)
            maxA = max(maxA, computed)
            if(height[i] < height[j]):
                i += 1
            else:
                j -= 1
        
        return maxA