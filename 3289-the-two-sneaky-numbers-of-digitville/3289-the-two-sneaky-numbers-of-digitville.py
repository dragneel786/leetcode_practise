class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[i] += 1
        
        for num in nums:
            idx = abs(num) - 1
            nums[idx] *= -1
        
        res = []
        size = len(nums) - 2
        for i, num in enumerate(nums[:size]):
            if num > 0 and i not in res:
                res.append(i)
        
        return res