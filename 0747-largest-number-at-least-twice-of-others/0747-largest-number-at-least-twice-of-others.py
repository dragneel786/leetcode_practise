class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        fmax = -inf
        smax = -inf
        idx = -1
        
        for i, num in enumerate(nums):
            if(fmax < num):
                smax = fmax
                fmax = num
                idx = i
            
            elif(smax < num):
                smax = num
        
        return idx if(fmax >= smax * 2) else -1