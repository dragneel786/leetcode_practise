class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for num in nums:
            idx = abs(num) - 1
            if(nums[idx] > 0):
                nums[idx] = (~nums[idx]) + 1
        
        res = []
        for i, num in enumerate(nums, 1):
            if(num > 0):
                res.append(i)
        
        return res
        
        