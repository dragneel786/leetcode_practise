class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        n = len(nums)
        prev = None
        for i in range(1, n):
            if(nums[i - 1] == nums[i]):
                continue
            
            if(prev is not None and prev != (nums[i - 1] < nums[i])):
                return False
            
            prev = nums[i - 1] < nums[i]
        return True