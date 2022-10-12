class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        sorted_nums = [nums[-1]]
        res = [0] * len(nums)
        
        for i in range(len(nums) - 2, -1, -1):
            idx = bisect_left(sorted_nums, nums[i])
            res[i] = idx
            insort(sorted_nums, nums[i])
        
        return res
    
        