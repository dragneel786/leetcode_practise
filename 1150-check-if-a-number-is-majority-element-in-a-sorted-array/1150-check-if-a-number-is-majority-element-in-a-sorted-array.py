class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        mcount = n // 2 + 1
        left = bisect_left(nums, target)
        right = bisect_right(nums, target)
        
        return right - left >= mcount
                