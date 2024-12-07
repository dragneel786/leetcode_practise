class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        nums = set(nums)
        yes = 0
        for v in nums:
            if v < k:
                return -1
            
            yes += v == k
            
        return len(nums) - yes
        
        