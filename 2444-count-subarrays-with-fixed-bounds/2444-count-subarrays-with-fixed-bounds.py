class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        ans = 0
        min_idx = max_idx = sub_end_idx = -1
        for i, num in enumerate(nums):
            if(num > maxK or num < minK): sub_end_idx = i
            if(num == minK): min_idx = i
            if(num == maxK): max_idx = i
            ans += max(0, min(min_idx, max_idx) - sub_end_idx)
        
        return ans