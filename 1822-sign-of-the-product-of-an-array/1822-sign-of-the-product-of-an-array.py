class Solution:
    def arraySign(self, nums: List[int]) -> int:
        prod = 1
        for num in nums:
            prod *= num
        
        return 0 if(not prod) else abs(prod) // prod
        