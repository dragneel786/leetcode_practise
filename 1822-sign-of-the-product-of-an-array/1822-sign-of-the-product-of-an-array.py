class Solution:
    def arraySign(self, nums: List[int]) -> int:
        prod = reduce(lambda x, y: x * y, nums)
        return 0 if(not prod) else abs(prod) // prod
        