class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        fmax = smax = 0
        for num in nums:
            if(fmax < num):
                smax, fmax = fmax, num
            
            elif(smax < num):
                smax = num
        
        return (fmax - 1) * (smax - 1)