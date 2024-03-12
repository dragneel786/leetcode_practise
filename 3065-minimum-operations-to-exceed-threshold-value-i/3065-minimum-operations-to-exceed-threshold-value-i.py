class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        counts = 0
        for num in nums:
            counts += num < k
        
        return counts
        