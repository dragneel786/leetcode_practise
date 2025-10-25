class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        ans = 0
        min_val = min(nums)
        max_val = max(nums)
        for _ in range(k):
            ans += (max_val - min_val)
        
        return ans