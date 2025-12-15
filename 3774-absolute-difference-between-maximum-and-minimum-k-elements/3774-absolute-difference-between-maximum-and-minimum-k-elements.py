class Solution:
    def absDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        sums = suml = 0
        for i in range(k):
            sums += nums[i]
            suml += nums[n - i - 1]
        
        return suml - sums