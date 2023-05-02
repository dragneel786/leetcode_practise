class Solution:
    def arraySign(self, nums: List[int]) -> int:
        prod = reduce(lambda x, y: x * y, nums)
        if(not prod):
            return 0
        
        return 1 if(prod > 0) else -1
        