class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums) + 1):
            idx = bisect_left(nums, i, 0, len(nums))
            # print((len(nums) - idx))
            if((len(nums) - idx) == i):
                return i
        
        return -1