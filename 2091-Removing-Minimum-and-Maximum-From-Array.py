class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        size = len(nums)
        max_idx = min_idx = 0
        for i, num in enumerate(nums):
            if num > nums[max_idx]:
                max_idx = i
            
            if num <= nums[min_idx]:
                min_idx = i
               
        mini, maxi = min(min_idx, max_idx), max(min_idx, max_idx)
        return min(maxi + 1, size - mini, mini + 1 + size - maxi)
