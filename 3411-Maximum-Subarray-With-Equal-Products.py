class Solution:
    def maxLength(self, nums: List[int]) -> int:
        for size in range(len(nums) - 1, 0, -1):
            pd = gd = lc = 0
            for i in range(size, len(nums)):
                if reduce(lambda x, y: x * y, nums[i - size: i + 1]) ==\
                 (gcd(*nums[i - size: i + 1]) * lcm(*nums[i - size: i + 1])):
                    return size + 1
        
        return 1
                