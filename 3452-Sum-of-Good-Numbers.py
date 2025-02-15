class Solution:
    def sumOfGoodNumbers(self, nums: List[int], k: int) -> int:
        size = len(nums)
        sums = 0
        for i, num in enumerate(nums):
            if i - k > -1 and num <= nums[i - k]:
                continue
            
            if i + k < size and num <= nums[i + k]:
                continue
            
            sums += num
        
        return sums