class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        size = len(nums)
        nums = nums[::-1] + nums + nums
        res = []
        for i in range(size, 2 * size):
            res.append(nums[i + (nums[i] % size)])
        
        return res