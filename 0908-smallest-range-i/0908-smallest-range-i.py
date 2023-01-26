class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        nums.sort()
        diff = nums[-1] - nums[0]
        if(diff <= (k * 2)):
            return 0
        
        return diff - (k * 2)
            