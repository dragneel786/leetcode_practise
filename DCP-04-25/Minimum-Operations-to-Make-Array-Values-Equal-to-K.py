class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        nums = sorted(list(set(nums)), reverse=True)
        if nums[-1] < k:
            return -1
        
        return len(nums) - (nums[-1] == k)

        