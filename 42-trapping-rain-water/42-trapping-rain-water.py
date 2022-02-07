class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n < 3:
            return 0
        l = height[0]
        r = height[n-1]
        i = 0
        j = n - 1  
        res = 0
        while i < j:
            if r < l:
                j -= 1
                if height[j] < r:
                    res += r - height[j]
                else:
                    r = height[j]
            else:
                i += 1
                if height[i] < l:
                    res += l - height[i] 
                else:
                    l = height[i]
        return res